from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .models import User, OTP
from .serializers import (
    RegistrationSerializer, 
    VerifyEmailSerializer, 
    UserSerializer, 
    UserLogInAPIViewSerializer
)
from .tasks import send_activation_email
from .utils import checkOTPExpiration


class RegistrationAPIView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            send_activation_email.delay(user.id)
            return Response({
                "message": "User registered successfully!",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyEmailAPIView(generics.CreateAPIView):
    serializer_class = VerifyEmailSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            otp = serializer.validated_data['otp']
            user = User.objects.filter(email=email).first()
            get_otp = OTP.objects.filter(otp=otp).first()

            if not user or not get_otp or not checkOTPExpiration(get_otp):
                return Response({
                    "message": "Invalid email or OTP, or OTP has expired."
                }, status=status.HTTP_400_BAD_REQUEST)

            user.is_active = True
            user.is_verified = True
            user.save()
            get_otp.delete()
            return Response({
                "message": "User verified successfully!"
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResendVerifyEmailAPIView(generics.CreateAPIView):
    serializer_class = VerifyEmailSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = User.objects.filter(email=email).first()

            if not user:
                return Response({
                    "message": "User with this email does not exist."
                }, status=status.HTTP_404_NOT_FOUND)

            if user.is_verified:
                return Response({
                    "message": "User already verified."
                }, status=status.HTTP_400_BAD_REQUEST)

            send_activation_email.delay(user.id)
            return Response({
                "message": "OTP sent successfully."
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class UserLoginAPIView(generics.CreateAPIView):
    serializer_class = UserLogInAPIViewSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(request, username=email, password=password)

            if not user:
                return Response({
                    "error": "Invalid Credentials"
                }, status=status.HTTP_401_UNAUTHORIZED)

            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserLogoutAPIView(APIView):
    
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            request.user.auth_token.delete()
            return Response({"message": "Logout successful."}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            # Consider logging the exception here for debugging purposes
            return Response({"error": "There was an error during logout. Please try again."}, status=status.HTTP_400_BAD_REQUEST)
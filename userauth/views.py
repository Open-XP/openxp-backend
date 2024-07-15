from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.contrib.auth.tokens import default_token_generator
from rest_framework.exceptions import ValidationError
from django.core.mail import send_mail
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .models import User, OTP
from .serializers import (
    RegistrationSerializer, 
    VerifyEmailSerializer, 
    UserSerializer, 
    UserLogInAPIViewSerializer,
    PasswordResetSerializer,
    SetNewPasswordSerializer
    
)
from .tasks import send_activation_email
from .utils import checkOTPExpiration


# class RegistrationAPIView(generics.CreateAPIView):
#     serializer_class = RegistrationSerializer
#     permission_classes = [AllowAny]

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             send_activation_email.delay(user.id)
#             return Response({
#                 "message": "User registered successfully!",
#                 "data": serializer.data
#             }, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# User Registration APIView (Temp fix)
class RegistrationAPIView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                "message": "User registered successfully!",
                "data": serializer.data,
                "token": token.key  
            }, status=status.HTTP_201_CREATED)
        else:
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
    
    
class PasswordResetAPIView(generics.GenericAPIView):
    serializer_class = PasswordResetSerializer
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user, created = User.objects.get_or_create(email=email)
            if not created:
                token_generator = PasswordResetTokenGenerator()
                token = token_generator.make_token(user)
                uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
                
                # Frontend URL for password reset confirmation
                # Update 'http://frontend.com' to the actual domain of your frontend application
                absurl = f'http://localhost:3000/confirm-password-reset/{uidb64}/{token}/'
                
                email_body = f'Hello, \nUse the link below to reset your password \n{absurl}'
                send_mail(
                    'Password Reset Request',
                    email_body,
                    'noreply@yourdomain.com',  # Update with your actual email
                    [email],
                    fail_silently=False,
                )
                return Response({'message': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)
            else:
                # Consider handling the case where the user does not exist
                pass
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# Password Reset Confirmation APIView
class PasswordResetConfirmAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = SetNewPasswordSerializer  # Keep your serializer for handling the password reset logic

    def post(self, request, *args, **kwargs):
        uidb64 = kwargs.get('uidb64')
        token = kwargs.get('token')

        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            serializer = self.serializer_class(data=request.data)  # Use the serializer to validate and save the new password
            
            if serializer.is_valid():
                user.set_password(serializer.validated_data['password'])
                user.save()
                return Response({"message": "Password has been reset successfully."}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            raise ValidationError({"message" :"Invalid token or user ID"})


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
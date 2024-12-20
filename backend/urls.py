from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static
# from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('userauth.urls')),
    path('api/exams/', include('exams.urls')),
    path('api/quiz/', include('quiz_manager.urls')),
    path('api/examscheduler/', include('examscheduler.urls')),
    path('api/ai/', include('ai.urls')),
    # path('', TemplateView.as_view(template_name='index.html')),
    # path('', include('main.urls')),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

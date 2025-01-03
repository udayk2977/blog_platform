"""
blog_project/urls.py
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # User Service
    path('api/', include('user_service.urls')),
    
    # Blog Service
    path('api/', include('blog_service.urls')),
    
    # Comment Service
    path('api/', include('comment_service.urls')),
]

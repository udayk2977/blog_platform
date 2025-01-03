# blog_service/settings.py

from .settings import *

# Service-specific configurations
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    # ... other necessary apps
    'rest_framework',
    'rest_framework_simplejwt',
    'blog_service',  # Only include the blog_service app
]

# comment_service/settings.py

from .settings import *

# Service-specific configurations
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    # ... other necessary apps
    'rest_framework',
    'rest_framework_simplejwt',
    'comment_service',  # Only include the comment_service app
]

# user_service/settings.py

from .settings import *

# Service-specific configurations can go here
# For example, restrict installed apps to user_service
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    # ... other necessary apps
    'rest_framework',
    'rest_framework_simplejwt',
    'user_service',  # Only include the user_service app
]

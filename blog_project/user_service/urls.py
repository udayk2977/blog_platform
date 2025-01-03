from django.urls import path
from .views import RegisterView, LoginView, UserDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),   # POST /register/
    path('login/', LoginView.as_view(), name='login'),           # POST /login/

    path('users/<int:id>/', UserDetailView.as_view(), name='user-detail'),  # GET, PUT, DELETE
]

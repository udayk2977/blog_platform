from django.urls import path
from .views import CommentCreateView, CommentListView

urlpatterns = [
    path('comments/', CommentCreateView.as_view(), name='comment-create'),  
    path('comments', CommentListView.as_view(), name='comment-list'),      
]

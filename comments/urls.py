from django.urls import path
from . import views


urlpatterns = [
    path('articles/<slug:slug>/comments/', views.CommentListCreateView.as_view(),name='comments_list'),
    path('comments/<int:pk>/', views.CommentDeleteView.as_view(),name='comment_delete'),
    
]
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from . import views



urlpatterns = [
    path('users/', views.RegisterUser.as_view(), name='register'),
    path('login/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),

    path('user/',views.CurrentUserView.as_view(),name='current_user'),
    path('profiles/<str:username>/',views.ProfileView.as_view(),name='profile_detail'),
    path('profiles/<str:username>/follow/',views.FollowToggleView.as_view(),name='follow_toggle'),
]
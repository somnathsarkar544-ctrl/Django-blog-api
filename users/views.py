from rest_framework import generics,permissions,status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import User
from .serializers import UserSerializer, ProfileSerializer
from django.shortcuts import render

# Create your views here.

class RegisterUser(generics.CreateAPIView):
    queryset = User.objects.all() # anyone can register
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self):
        return self.request.user

class CurrentUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated] # only logged in users can access

    def get_object(self):
        return self.request.user
    

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.AllowAny]
    queryset=User.objects.all()
    lookup_field = 'username'


class FollowToggleView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileSerializer
    queryset = User.objects.all()
    lookup_field = 'username'

    def post(self,request,username): # follow user
        target = get_object_or_404(User, username=username)
        if request.user == target:
            return Response({'detail':"You can't follow yourself."},status=status.HTTP_400_BAD_REQUEST)
        target.followers.add(request.user)
        serializer = self.get_serializer(target, context={'request':request}) # pass request to serializer to check if current user is following
        return Response(serializer.data)
    
    def delete(self,request,username): # unfollow user
        target = get_object_or_404(User, username=username)
        target.followers.remove(request.user)
        serializer = self.get_serializer(target, context={'request':request})
        return Response(serializer.data)
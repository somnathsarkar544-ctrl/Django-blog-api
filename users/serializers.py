from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,required=True)

    class Meta:
        model=User
        fields= ('id','username','email','password','bio','image','created_at') # what fields are allowed 
        read_only_fields = ('id','created_at')                                  # what fields can't be changed

    def create(self, validated_data):
        password = validated_data.pop('password')# remove password from validated data
        user = User(**validated_data) # create user instance without saving to db
        user.set_password(password) # hashes password securely 
        user.save() # save user to db
        return user 

class ProfileSerializer(serializers.ModelSerializer):# for viewing other users's profiles
    following = serializers.SerializerMethodField(read_only = True) # to check if current user is following this profile user

    class Meta: 
        model = User
        fields =('username','bio','image','following')
        read_only_fields = ['username','following']
    
    def get_following(self,obj):# profile beimg viewed
        request = self.context.get('request') # get current logged in user
        if not request or request.user.is_anonymous: # guest user always false
            return False
        return obj.followers.filter(pk=request.user.pk).exists()



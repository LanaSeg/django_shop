from django.contrib.auth.models import User
from rest_framework import serializers
from app_users.models import Profile


class ProfileAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['avatar']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['fullName', 'phone', 'email', 'avatar']


class UserPasswordChangeSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['password']

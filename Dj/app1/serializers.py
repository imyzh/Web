from rest_framework import serializers

class UserInfoSer(serializers.Serializer):
    username = serializers.CharField()
    token = serializers.CharField()
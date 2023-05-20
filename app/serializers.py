from rest_framework import serializers
from .models import user,todo



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['name','email','password','is_deleted']


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = todo
        fields = ['title','desc','user','img']        
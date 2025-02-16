from rest_framework import serializers
from .models import Admin

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

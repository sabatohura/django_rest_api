from rest_framework import fields, serializers
from core.models import Currency, Category, User, imageProfile
class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency 
        fields = ("id", "code", "name")
class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "location", "phone","fullname")
class imageProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = imageProfile
        fields = ("id", "imagename","userId","uploadedate")
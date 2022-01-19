from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet    
from rest_framework import routers

from core.models import Category, Currency, User, imageProfile
from core.serializers import CurrencySerializer, categorySerializer, imageProfileSerializer, userSerializer

# Create your views here.
class CurrencyListAPIView(ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class=categorySerializer
class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userSerializer
class imageProfileModelViewSet(ModelViewSet):
    queryset = imageProfile.objects.all()
    serializer_class = imageProfileSerializer


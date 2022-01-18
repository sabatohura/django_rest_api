from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet    
from rest_framework import routers

from core.models import Category, Currency, User
from core.serializers import CurrencySerializer, categorySerializer, userSerializer

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

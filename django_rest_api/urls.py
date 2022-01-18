
from django.contrib import admin
from django.urls import path
from core import views
from rest_framework import routers
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
router = routers.SimpleRouter()
router.register(r'categories', views.CategoryModelViewSet, basename="category"),
router.register(r'users', views.UserModelViewSet, basename ="user")
urlpatterns = [ 
    path('currencies/', views.CurrencyListAPIView.as_view(), name="currencies"),

] + router.urls
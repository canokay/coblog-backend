from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

app_name = 'blog'
router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
]
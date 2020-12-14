from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from blog.models import Blog

class BlogListSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id','title','slug','content','is_active']


class BlogDetailSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title','slug','content','is_active']

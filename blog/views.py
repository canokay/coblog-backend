from blog.models import Blog
from blog.serializers import BlogListSerializer, BlogDetailSerializer
from rest_framework import viewsets
from rest_framework.views  import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

"""
class BlogListView(APIView):
    def get(self, request, format=None):
        blogs = Blog.objects.all()
        serializer = BlogListSerializer(blogs, many=True)
        return Response(serializer.data)
"""

class BlogListView(ListAPIView):
    serializer_class = BlogListSerializer

    def get_queryset(self):
        return Blog.objects.all()



class BlogDetailView(APIView):
    def get(self, request, *args, **kwargs):
        blog = Blog.objects.filter(id=self.kwargs['id'])
        serializer = BlogDetailSerializer(blog, many=True)
        return Response(serializer.data)

class BlogSearchView(APIView):
    def get(self, request, format=None):
        blog = Blog.objects.filter(title=self.kwargs['title'])
        
        serializer_class = BlogListSerializer


    def post(self, request, format=None):
        pass


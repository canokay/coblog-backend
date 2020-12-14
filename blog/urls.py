from django.conf.urls import url
from django.urls import include
from rest_framework import routers
from blog.views import BlogListView,BlogDetailView

app_name = 'blog'
router = routers.DefaultRouter()

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^blog/$', BlogListView.as_view()),
    url(r'^blog/(?P<id>\d+)/$', BlogDetailView.as_view()),
]
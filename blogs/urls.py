from django.urls import path
from .views import post_blog,update_blog,delete_blog,BlogViewSet
from rest_framework import routers
app_name = 'blogs'
router = routers.DefaultRouter()
router.register(r'', BlogViewSet) 
urlpatterns = [
    path('create',post_blog,name='create_blog'),
    path('update/<int:pk>/', update_blog, name='update_blog'),
    path('<int:pk>/delete/', delete_blog, name='delete_blog'),
]+router.urls

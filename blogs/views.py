from rest_framework.decorators import api_view
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from django.shortcuts import get_object_or_404

from .models import Blog
from .serializers import BlogSerializer
# Create your views here.
# all actions for blog

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
 
    
# @api_view(['GET'])
# def get_blogs(request):
#     if request.query_params:
#         blog_queryset = Blog.objects.filter(**request.query_params.dict())
#     else:
#         blog_queryset = Blog.objects.all()

#     if blog_queryset:
#         serializer = BlogSerializer(blog_queryset, many=True)
#         return Response(serializer.data)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
# get blog by id
# @api_view(['GET'])
# def get_blog(request,pk):
#     print("k",pk)
#     blog_queryset = Blog.objects.filter(id=pk)
#     serializer = BlogSerializer(blog_queryset, many=False)
#     print(serializer)
#     return  Response(serializer.data.get('title'))
#     # if blog_queryset:
#     #     serializer = BlogSerializer(blog_queryset, many=False)
#     #     return Response(serializer.data)
#     # else:
#     #     return Response({"error":"there is no a blog with this id"})
    
# # create blog

@api_view(['POST'])
def post_blog(request):
    blog_queryset = BlogSerializer(data=request.data)
    if Blog.objects.filter(**request.data).exists():
        raise serializers.ValidationError({'error':'This data already exists'}) 
    
    if request.data.get('title')=='':
          raise serializers.ValidationError({"error":'The title must not be empty write smth'}) 
      
    if request.data.get('description')=='':
          raise serializers.ValidationError({'error':'The description must not be empty write smth'}) 
       
    if blog_queryset.is_valid():
        blog_queryset.save()
        return Response({"message":"added data"})
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
# update blog  
@api_view(['PUT'])
def update_blog(request, pk):
    get_data = Blog.objects.get(pk=pk)
    data = BlogSerializer(instance=get_data, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
# delete
@api_view(['DELETE'])
def delete_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
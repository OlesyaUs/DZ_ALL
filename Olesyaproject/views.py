from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Olesyaproject.Serializer import PostSerializer, CommentSerializer
from Olesyaproject.models import Post, Comment


@api_view(['GET'])
def get_allPost(request):
    post = Post.objects.all()
    data = PostSerializer(post, many=True).data
    return Response(data=data)


@api_view(['GET'])
def get_PostID(request, id):
    post = Post.objects.get(id=id)
    data = PostSerializer(post).data
    return Response(data=data)


@api_view(['GET'])
def get_CommentID(request, id):
    comment = Comment.objects.get(id=id)
    data = CommentSerializer(comment).data
    return Response(data=data)


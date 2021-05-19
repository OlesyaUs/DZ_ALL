import serializer as serializer

from Olesyaproject.models import Post, Comment
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = 'id name text created_date'.split()


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = 'id text'.split()


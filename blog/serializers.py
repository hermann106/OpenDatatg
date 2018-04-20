from django.contrib.auth.models import User, Group
from rest_framework import serializers
from . models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    comments = serializers.StringRelatedField(many=True)

    class Meta:
        model = Post
        fields = ('title','slug','description','picture','owner','publish','created','updated','status','comments')


# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields=('post','name','email','body','active','created')

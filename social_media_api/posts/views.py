from django.shortcuts import render
from rest_framework import viewsets
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

# Create your views here.


class PostViewset(viewsets.ModelViewset):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewset(viewsets.ModelViewset):
    queryset = Comment.objects.all()
    serializer_class =CommentSerializer
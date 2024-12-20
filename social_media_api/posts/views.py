from django.shortcuts import render
from rest_framework import viewsets
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class =CommentSerializer


class FeedView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()  # Explicitly assign to a variable
        return Post.objects.filter(author__in=following_users).order_by('-created_at')  # Use 'following_users'

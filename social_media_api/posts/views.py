from django.shortcuts import render
from rest_framework import viewsets
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from accounts.models import CustomUser
# Create your views here.


class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class =CommentSerializer


class FeedView(GenericAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Get the current user
        user = self.request.user

        # Ensure the user is a CustomUser instance
        following_users = CustomUser.objects.filter(pk__in=user.following.all())
        
        # Filter posts by users the current user follows
        return Post.objects.filter(author__in=following_users).order_by('-created_at')

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

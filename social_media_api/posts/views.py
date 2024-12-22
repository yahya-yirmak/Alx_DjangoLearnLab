from django.shortcuts import render
from rest_framework import viewsets
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.generics import ListAPIView
from rest_framework import generics, permissions
from rest_framework.response import Response
from posts.models import Post, Like
from rest_framework import status
from notifications.models import Notification
# Create your views here.


class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class =CommentSerializer


class FeedView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')



class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        pk = request.data.get('id')
        try:
            post = post = generics.get_object_or_404(Post, pk=pk)
            like, created = Like.objects.get_or_create(user=request.user, post=post)
            if created:
                Notification.objects.create(
                recipient=post.user,
                actor=request.user,   
                verb="liked your post", 
                target=post           
            )
                return Response({'detail':'Post liked successfully.'}, status=status.HTTP_200_OK)
            return Response({'detail':'You can not like multiple times'}, status=status.HTTP_400_BAD_REQUEST)
        
        except Post.DoesNotExist:
            return Response({'detail':'Post not found'}, status=status.HTTP_404_NOT_FOUND)


class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        pk = request.data.get('id')
        try:
            post = Post.objects.get(id=pk)
            like = Like.objects.get(post=post, liked_by=request.user)
            like.delete()
            return Response({'message':'Post unliked succefully.'}, status=status.HTTP_200_OK)
        except Like.DoesNotExist:
            return Response({'message':'Like not found'}, status=status.HTTP_404_NOT_FOUND)

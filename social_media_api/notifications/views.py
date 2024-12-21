from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from posts.models import Post, Like
from rest_framework import status
from notifications.models import Notification


# Create your views here.

class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        pk = request.data.get('post_id')
        try:
            post = post = generics.get_object_or_404(Post, pk=pk)
            like, created = Like.objects.get_or_create(post=post, liked_by = request.user)
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
        post_id = request.data.get('post_id')
        try:
            post = Post.objects.get(id=post_id)
            like = Like.objects.get(post=post, liked_by=request.user)
            like.delete()
            return Response({'message':'Post unliked succefully.'}, status=status.HTTP_200_OK)
        except Like.DoesNotExist:
            return Response({'message':'Like not found'}, status=status.HTTP_404_NOT_FOUND)
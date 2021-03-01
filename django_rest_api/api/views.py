from django.db.models import fields
from django.shortcuts import render
from rest_framework import generics, serializers, status
from .models import Post
from .serializers import PostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class GetPostsView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class GetPostView(generics.UpdateAPIView):
    serializer_class = PostSerializer

    def get(self, request, id):
        if id != None:
            post = Post.objects.filter(id=id)
            if len(post) > 0:
                data = PostSerializer(post[0]).data
                return Response(data, status=status.HTTP_200_OK)
            return Response({'message': 'Invalid ID.'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'message': 'ID missing in URL params'}, status=status.HTTP_400_BAD_REQUEST)


class CreatePostView(APIView):
    serializer_class = PostSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            title = serializer.data.get('title')
            author = serializer.data.get('author')
            content = serializer.data.get('content')
            post = Post(title=title, author=author, content=content)
            post.save()

            return Response(PostSerializer(post).data, status=status.HTTP_201_CREATED)

        return Response({'message': 'Invalid input.'}, status=status.HTTP_400_BAD_REQUEST)


class UpdatePostView(APIView):
    serializer_class = PostSerializer

    def put(self, request, id):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            title = serializer.data.get('title')
            author = serializer.data.get('author')
            content = serializer.data.get('content')

            queryset = Post.objects.filter(id=id)
            if not queryset.exists():
                return Response({'message': 'Post not found.'}, status=status.HTTP_404_NOT_FOUND)

            post = queryset[0]
            post.title = title
            post.author = author
            post.content = content
            post.save()
            return Response(PostSerializer(post).data, status=status.HTTP_200_OK)

        return Response({'message': 'Invalid input.'}, status=status.HTTP_400_BAD_REQUEST)


class DeletePostView(generics.DestroyAPIView):
    def delete(self, request, id):
        post = Post.objects.get(id=id)
        if not post:
            return Response({'message': 'Post not found.'}, status=status.HTTP_404_NOT_FOUND)
        else:
            post.delete()

        return Response({'message': 'Success'}, status=status.HTTP_200_OK)

from django.urls import path
from .views import DeletePostView, GetPostsView, CreatePostView, GetPostView, UpdatePostView

urlpatterns = [
    path('posts', GetPostsView.as_view()),
    path('post', GetPostView.as_view()),
    path('create-post', CreatePostView.as_view()),
    path('update-post', UpdatePostView.as_view()),
    path('delete-post', DeletePostView.as_view())
]

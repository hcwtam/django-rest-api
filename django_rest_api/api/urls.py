from django.urls import path
from .views import DeletePostView, GetPostsView, CreatePostView, GetPostView, UpdatePostView

urlpatterns = [
    path('', GetPostsView.as_view()),
    path('<str:id>/', GetPostView.as_view()),
    path('create', CreatePostView.as_view()),
    path('update/<str:id>/', UpdatePostView.as_view()),
    path('delete/<str:id>/', DeletePostView.as_view())
]

from django.urls import path
from .views import LikePostView, UnlikePostView, FeedView
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

#router = DefaultRouter()
#router.register(r'posts', PostViewSet, basename='post')
#router.register(r'comments', CommentViewSet, basename='comment')


#urlpatterns = [
#    path('feed/', FeedView.as_view(), name='feed'),
#]

#urlpatterns += router.urls




router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('posts/<int:pk>/like/', LikePostView.as_view()),
    path('posts/<int:pk>/unlike/', UnlikePostView.as_view()),
    path('feed/', FeedView.as_view()),
]

urlpatterns += router.urls

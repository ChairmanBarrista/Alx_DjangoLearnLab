from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet


router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')


urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),

    # Token endpoint
    path('get-token/', obtain_auth_token, name='get-token'),

    # ViewSet router URLs
    path('', include(router.urls)),
]

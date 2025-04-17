from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, GroupViewSet
from rest_framework.authtoken.views import obtain_auth_token

# Создание и настройка роутера
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')

urlpatterns = [
    # Путь для получения токена
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

    # Путь для работы с ресурсами (посты, группы и т.д.)
    path('', include(router.urls)), # Измените на пустую строку, так как 'api/v1/' уже определен в корневом urls.py

    # Путь для работы с комментариями
    path('posts/<int:post_id>/comments/', CommentViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='comment-list'),
    path('posts/<int:post_id>/comments/<int:pk>/', CommentViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='comment-detail'),
]
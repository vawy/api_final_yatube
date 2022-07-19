from django.shortcuts import get_object_or_404
from rest_framework import (viewsets,
                            permissions,
                            filters,
                            mixins,
                            pagination)

from posts.models import Post, Group, Comment
from .serializers import (PostSerializer,
                          GroupSerializer,
                          CommentSerializer,
                          FollowSerializer)
from .permissions import AuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    """
    Представление модели Post.
    Для неавторизованных пользователей - только чтение.
    Для авторизованных пользователей - весь CRUD функционал.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly,)
    pagination_class = pagination.LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Представление модели Group.
    Доступ только для чтения.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
    Представление для модели Comment.
    Обрабатывает все CRUD запросы.
    """
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        new_queryset = post.comments.all()
        return new_queryset

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """
    Представление модели Follow.
    Доступ только для авторизованных пользователей.
    Обрабатывает только GET и POST запросы.
    Возможен поиск.
    """
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username', 'user__username')

    def get_queryset(self):
        user = self.request.user
        return user.followers.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

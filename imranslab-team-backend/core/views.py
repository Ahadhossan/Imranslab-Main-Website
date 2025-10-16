from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.parsers import MultiPartParser, FormParser

from . import models, serializers
from .pagination import DefaultPagination
from .permissions import IsOwnerOrReadOnly, IsUserOrReadOnly

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    parser_classes = [MultiPartParser, FormParser]  # Add these parsers
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [IsUserOrReadOnly]
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['role']
    search_fields = ['first_name', 'last_name', 'email', 'username']


class SocialMediaLinksViewSet(viewsets.ModelViewSet):
    queryset = models.SocialMediaLink.objects.all()
    serializer_class = serializers.SocialMediaLinksSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_serializer_context(self):
        return {'user_id': self.kwargs['user_pk']}

    def get_queryset(self):
        user_id = self.kwargs['user_pk']
        print(user_id)
        return models.SocialMediaLink.objects.filter(user_id=user_id)


class CoreTechnologiesViewSet(viewsets.ModelViewSet):
    queryset = models.CoreTechnologie
    serializer_class = serializers.CoreTechnologiesSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_serializer_context(self):
        return {'user_id': self.kwargs['user_pk']}

    def get_queryset(self):
        user_id = self.kwargs['user_pk']
        return models.CoreTechnologie.objects.filter(user_id=user_id)


class ProjectsContributedToViewSet(viewsets.ModelViewSet):
    queryset = models.ProjectsContributedTo
    serializer_class = serializers.ProjectsContributedToSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_serializer_context(self):
        return {'user_id': self.kwargs['user_pk']}

    def get_queryset(self):
        user_id = self.kwargs['user_pk']
        return models.ProjectsContributedTo.objects.filter(user_id=user_id)


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = models.Article
    serializer_class = serializers.ArticleSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_serializer_context(self):
        return {'user_id': self.kwargs['user_pk']}

    def get_queryset(self):
        user_id = self.kwargs['user_pk']
        return models.Article.objects.filter(user_id=user_id)


class ContributionViewSet(viewsets.ModelViewSet):
    queryset = models.Contribution
    serializer_class = serializers.ContributionSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_serializer_context(self):
        return {'user_id': self.kwargs['user_pk']}

    def get_queryset(self):
        return models.Contribution.objects.filter(user_id=self.kwargs['user_pk'])

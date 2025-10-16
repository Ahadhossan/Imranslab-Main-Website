from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter

from . import views

router = DefaultRouter()
router.register('users', views.UserViewSet, basename='users')

user_nested_router = NestedDefaultRouter(router, 'users', lookup='user')
# Nested router for SocialMediaLinks under the user's profile
user_nested_router.register(
    'socialmedialinks', views.SocialMediaLinksViewSet, basename='social-media-links')
# Nested router for CoreTechnologies under the user's profile
user_nested_router.register(
    'coretechnologies', views.CoreTechnologiesViewSet, basename='core-technologies')
# Nested router for ProjectsContributedTo under the user's profile
user_nested_router.register(
    'projectscontributed', views.ProjectsContributedToViewSet, basename='projects-contributed-to')
# Nested router for Article under the user's profile
user_nested_router.register(
    'article', views.ArticleViewSet, basename='article')
# Nested router for Contribution under the user's profile
user_nested_router.register(
    'contribution', views.ContributionViewSet, basename='contribution')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(user_nested_router.urls)),
]

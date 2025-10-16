from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer
from rest_framework import serializers
from . import models


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password',
                  'email']


class UserSerializer(BaseUserSerializer):
    # Add a field for social media links
    socialmedialinks = serializers.SerializerMethodField()
    coretechnologies = serializers.SerializerMethodField()
    projectscontributedto = serializers.SerializerMethodField()
    articles = serializers.SerializerMethodField()
    contributions = serializers.SerializerMethodField()

    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'first_name', 'last_name', 'role', 'socialmedialinks', 'coretechnologies', 'projectscontributedto', 'articles',
                  'contributions', 'personalinterests', 'aboutme', 'username', 'email', 'position', 'address', 'phone', 'birth_date', 'image']
        extra_kwargs = {
            'image': {'required': False}  # Make image optional
        }

     # Method to get core socialmedialinks
    def get_socialmedialinks(self, obj):
        social_links = models.SocialMediaLink.objects.filter(user=obj)
        return SocialMediaLinksSerializer(social_links, many=True).data

    # Method to get core technologies
    def get_coretechnologies(self, obj):
        core_techs = models.CoreTechnologie.objects.filter(user=obj)
        return CoreTechnologiesSerializer(core_techs, many=True).data

    # Method to get projects contributed to
    def get_projectscontributedto(self, obj):
        projects = models.ProjectsContributedTo.objects.filter(user=obj)
        return ProjectsContributedToSerializer(projects, many=True).data

    # Method to get articles
    def get_articles(self, obj):
        articles = models.Article.objects.filter(user=obj)
        return ArticleSerializer(articles, many=True).data

    # Method to get contributions
    def get_contributions(self, obj):
        contributions = models.Contribution.objects.filter(user=obj)
        return ContributionSerializer(contributions, many=True).data


class SocialMediaLinksSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user_id = self.context['user_id']
        return models.SocialMediaLink.objects.create(user_id=user_id, **validated_data)

    class Meta:
        model = models.SocialMediaLink
        fields = ['id', 'link', 'socialmediachoice']


class CoreTechnologiesSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user_id = self.context['user_id']
        return models.CoreTechnologie.objects.create(user_id=user_id, **validated_data)

    class Meta:
        model = models.CoreTechnologie
        fields = ['id', 'technology']


class ProjectsContributedToSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user_id = self.context['user_id']
        return models.ProjectsContributedTo.objects.create(user_id=user_id, **validated_data)

    class Meta:
        model = models.ProjectsContributedTo
        fields = ['id', 'technologies', 'description',
                  'projectlink', 'image', 'created_at']


class ArticleSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user_id = self.context['user_id']
        return models.Article.objects.create(user_id=user_id, **validated_data)

    class Meta:
        model = models.Article
        fields = ['id', 'title', 'description',
                  'articlelink', 'created_at', 'image']


class ContributionSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return models.Contribution.objects.create(user_id=self.context['user_id'], **validated_data)

    class Meta:
        model = models.Contribution
        fields = ['id', 'keys']

from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.


class User(AbstractUser):
    class RoleChoice(models.TextChoices):
        INTERN = 'intern', 'Intern'
        EXPERTS = 'experts', 'Experts'
        DIRECTORS = 'directors', 'Directors'

    email = models.EmailField(unique=True)
    position = models.CharField(max_length=255)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=255)
    personalinterests = models.TextField()
    aboutme = models.TextField()
    birth_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='user/images', null=True, blank=True)
    role = models.CharField(
        max_length=20,
        choices=RoleChoice.choices,
        default=RoleChoice.INTERN
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['first_name', 'last_name']


class SocialMediaLink(models.Model):
    class SocialMediaChoice(models.TextChoices):
        GITHUB = 'github', 'GitHub'
        LINKEDIN = 'linkedin', 'LinkedIn'
        FACEBOOK = 'facebook', 'FaceBook'
        X = 'x', 'X'
        OTHER = 'other', 'Other'

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='socialmedialinks')
    link = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    socialmediachoice = models.CharField(
        max_length=20,
        choices=SocialMediaChoice.choices,
        default=SocialMediaChoice.OTHER
    )

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class CoreTechnologie(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='technologiesuser')
    technology = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class ProjectsContributedTo(models.Model):
    class RoleChoice(models.TextChoices):
        INTERN = 'intern', 'Intern'
        DEVELOPER = 'developer', 'Developer'
        CONTRIBUTOR = 'contributor', 'Contributor'

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='contributedtouser')
    technologies = models.CharField(max_length=255)
    description = models.TextField()
    projectlink = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='projects/images', null=True, blank=True)
    role = models.CharField(
        max_length=20,
        choices=RoleChoice.choices,
        default=RoleChoice.INTERN
    )

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Article(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='articleuser')
    title = models.CharField(max_length=255)
    description = models.TextField()
    articlelink = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='article/images', null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Contribution(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='userContributions')
    keys = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

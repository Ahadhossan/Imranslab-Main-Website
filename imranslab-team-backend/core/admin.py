from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . import models
# Register your models here.


@admin.register(models.User)
class UserAmin(BaseUserAdmin):
    list_editable = ['role']
    list_display = ['username', 'first_name', 'last_name', 'role',
                    'email', 'position', 'address', 'phone', 'image']
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("first_name", "last_name", "username",  "email", "usable_password", "password1", "password2", ),
            },
        ),
    )


@admin.register(models.SocialMediaLink)
class SocialMediaLinks(admin.ModelAdmin):
    autocomplete_fields = ['user']
    list_display = ['user', 'link', 'socialmediachoice']
    list_editable = ['socialmediachoice']
    list_per_page = 20


@admin.register(models.CoreTechnologie)
class CoreTechnologiesAdmin(admin.ModelAdmin):
    autocomplete_fields = ['user']
    list_display = ['user', 'technology']
    list_per_page = 20


@admin.register(models.ProjectsContributedTo)
class ProjectsContributedToAdmin(admin.ModelAdmin):
    autocomplete_fields = ['user']
    list_display = ['user', 'technologies', 'role',
                    'projectlink', 'description', 'image']
    list_editable = ['role']
    list_per_page = 20


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    autocomplete_fields = ['user']
    list_display = ['user', 'title', 'description',
                    'articlelink']
    search_fields = ['user__first_name', 'user__last_name',
                     'title', 'articlelink']
    list_filter = ['created_at']
    list_per_page = 20


@admin.register(models.Contribution)
class ContributionAdmin(admin.ModelAdmin):
    autocomplete_fields = ['user']
    list_display = ['user', 'keys']
    list_filter = ['created_at']
    list_per_page = 20

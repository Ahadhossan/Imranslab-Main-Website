# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('nid/', views.nid_list, name='nid_list'),
#     path('passport/', views.passport_list, name='passport_list'),
#     path('license/', views.license_list, name='license_list'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.govt_identification_home, name='govt_identification_home'),
    path('nid/', views.nid_list, name='nid_list'),
    path('nid/add/', views.nid_add, name='nid_add'),
    path('nid/edit/<int:pk>/', views.nid_edit, name='nid_edit'),
    path('nid/delete/<int:pk>/', views.nid_delete, name='nid_delete'),

    path('passport/', views.passport_list, name='passport_list'),
    path('passport/add/', views.passport_add, name='passport_add'),
    path('passport/edit/<int:pk>/', views.passport_edit, name='passport_edit'),
    path('passport/delete/<int:pk>/', views.passport_delete, name='passport_delete'),

    path('license/', views.license_list, name='license_list'),
    path('license/add/', views.license_add, name='license_add'),
    path('license/edit/<int:pk>/', views.license_edit, name='license_edit'),
    path('license/delete/<int:pk>/', views.license_delete, name='license_delete'),
]

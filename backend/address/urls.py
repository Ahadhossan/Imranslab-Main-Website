from django.urls import path, include
from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     path('', views.index, name='index'),  # A sample URL for testing
# ]
from . import views
from .views import AddressViewSet

# why this DefaultRouter() is used?
# The DefaultRouter class automatically creates the URL patterns for the viewset actions.
# The router.register() method is used to register the viewset with the router.
# The r'addresses' argument is the base URL pattern for the viewset actions.
# The router.urls attribute is used to include the URL patterns in the project's URL configuration.
# The include() function is used to include the router URLs in the project's URL configuration.
# The path() function is used to define a URL pattern.
# The first argument is the URL pattern.
# The second argument is the view function.
# The third argument is the name of the URL pattern.

router = DefaultRouter()  # Create a router
router.register(r'addresses', AddressViewSet)

urlpatterns = [
    path('address/', include(router.urls)),  # Include the router URLs
    path('', views.address_list, name='address_list'),  # A sample URL for testing
    path('create/', views.create_address, name='create_address'),
    path('update/<int:pk>/', views.update_address, name='update_address'),
    path('delete/<int:pk>/', views.delete_address, name='delete_address'),
    path('api/bulk_create/', views.bulk_create_addresses, name='bulk_create_addresses'),
]

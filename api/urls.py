from django.urls import path
from . import views

urlpatterns = [
    path("testHello/", views.test_endpoint, name='testingEndpoint'),
    path("products/", views.ProductView.as_view(), name="ProductViewEndpoint"),
    path("product_details/<int:pk>/", views.ProductDetails.as_view(), name="ProductDetailsEndpoint"),
]
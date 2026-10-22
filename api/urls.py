from django.urls import path
form . import views

urlpatterns = [
    path("testHello", views.test_endpoint, name='testingEndpoint')
]
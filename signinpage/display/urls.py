from django.urls import path

from .import views

urlpatterns = [
    path('display/', views.signin, name="display"),
    path('submit/', views.submitUser, name="submit")
]

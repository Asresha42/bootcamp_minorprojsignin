from django.urls import path

from . import views

urlpatterns = [
    path('', views.signin, name="display"),
    path('submit/', views.submitUser, name="submit"),
    path('signup/', views.signup, name="signup"),
    path('fetch/', views.sUser, name="getu"),
]

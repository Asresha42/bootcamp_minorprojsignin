from django.urls import path
from .views import UserApiView
from .views import homePageView

urlpatterns = [
    path('', homePageView, name='home'),
    path('login/', UserApiView.as_view()),
    path('login/<int:pk>', UserApiView.as_view()),
]

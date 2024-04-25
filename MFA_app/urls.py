from django.urls import path

from .views import Register, Users

urlpatterns = [
    path('', Register.as_view(), name='register'),
    path('users', Users.as_view(), name='users'),
]
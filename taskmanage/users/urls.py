from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.SingUp.as_view(), name='signup'),
    path('profile/<int:pk>/', views.ProfileUpdateView.as_view(), name='profile')
]
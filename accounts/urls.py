from django.urls import path
from .views import ProfileDetailView, ProfileUpdateView, ProfileDeleteView, RegisterView
from . import views

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileDetailView.as_view(), name='profile'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
    path('profile/delete/', ProfileDeleteView.as_view(), name='profile_delete'),
    # ... other URLs
]
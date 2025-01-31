from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser
from .forms import CustomUserChangeForm



class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'registration/profile.html'

    def get_object(self):
        return self.request.user  # Display the logged-in user's profile

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'registration/profile_edit.html'
    success_url = reverse_lazy('profile')


    def get_object(self):
        return self.request.user  # Allow user to edit their own profile

class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    template_name = 'registration/profile_delete.html'
    success_url = reverse_lazy('login')  # Redirect to login after deletion

    def get_object(self):
        return self.request.user  # Allow user to delete their own account
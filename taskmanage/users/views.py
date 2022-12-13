from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic import UpdateView
from . import models

from .forms import CustomUserCreationForm
class SingUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = models.CustomUser
    fields = ['first_name', 'last_name', 'email', 'phone', 'username']
    template_name = 'profile.html'
    update_url = 'profile.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('profile', args="1")
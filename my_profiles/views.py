from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from .forms import MyProfileForm
from .models import MyProfile

@method_decorator(login_required, name='dispatch')
class MyProfileUpdateView(UpdateView):
    model = MyProfile
    form_class = MyProfileForm
    template_name = 'my_profiles/my_profile.html'
    success_url = reverse_lazy('my_profile')

    def get_object(self):
        object,created = MyProfile.objects.get_or_create(id=self.request.user.id)
        return object

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.user = self.request.user
        profile.id = self.request.user.id
        profile.save()
        return redirect('my_profile')

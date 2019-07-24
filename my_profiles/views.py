from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from .forms import MyProfileForm
from .models import MyProfile
import hashlib

@method_decorator(login_required, name='dispatch')
class MyProfileUpdateView(UpdateView):
    model = MyProfile
    form_class = MyProfileForm
    context_object_name = 'profile'
    template_name = 'my_profiles/my_profile.html'
    success_url = reverse_lazy('my_profile')

    def get_object(self):
        object,created = MyProfile.objects.get_or_create(id=self.request.user.id)
        if created:
            object.identicon = self.get_identicon()
            object.save()
        return object

    def get_identicon(self):
        email = self.request.user.email
        email_hash = hashlib.md5(email.lower().encode('utf-8')).hexdigest()
        return "http://www.gravatar.com/avatar/{0}?&r=PG&s=200&default=identicon".format(email_hash)

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.user = self.request.user
        profile.id = self.request.user.id
        profile.identicon = self.get_identicon()
        profile.save()
        return redirect('my_profile')

@login_required
def delete_img(request):
    if request.method == "POST":
        id = request.user.id
        profile = MyProfile.objects.get(pk=id)
        profile.img.delete(save=True)
        return redirect('my_profile')

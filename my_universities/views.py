from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from .forms import MyUniversityForm
from .models import MyUniversity

@method_decorator(login_required, name='dispatch')
class MyUniversityUpdateView(UpdateView):
    model = MyUniversity
    form_class = MyUniversityForm
    template_name = 'my_universities/my_university.html'
    success_url = reverse_lazy('my_university')

    def get_object(self):
        object,created = MyUniversity.objects.get_or_create(id=self.request.user.id)
        return object

    def form_valid(self, form):
        university = form.save(commit=False)
        university.user = self.request.user
        university.save()
        return redirect('my_university')

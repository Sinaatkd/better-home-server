from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model
from django.views.generic import ListView, CreateView, UpdateView


from .forms import CreateUserForm, UpdateUserForm, ChangeUserPasswordForm

User = get_user_model()


class AllUsersListView(ListView):
    model = User
    paginate_by = 30
    template_name = 'user/user_list.html'

    def get_queryset(self):
        search = self.request.GET.get('search', '')
        object_list = self.model.objects.all().order_by('-id')
        if search:
            object_list = self.model.objects.search_user_by_username_or_phone_number(search).order_by('-id')
        return object_list

class CreateUserView(CreateView):
    model = User
    form_class = CreateUserForm
    template_name = 'user/user_form.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.set_password(obj.password)
        obj.save()
        return HttpResponseRedirect(reverse('users_list'))


class ConsultantUsersListView(ListView):
    model = User
    paginate_by = 30
    template_name = 'user/user_list.html'

    def get_queryset(self):
        search = self.request.GET.get('search', '')
        object_list = self.model.objects.filter(is_consultant=True).order_by('-id')
        if search:
            object_list = self.model.objects.search_user_by_username_or_phone_number(search).filter(is_consultant=True).order_by('-id')
        return object_list

class UserUpdateView(UpdateView):
    model = User
    form_class = UpdateUserForm
    template_name = 'user/user_form.html'
    success_url = reverse_lazy('users_list')


class ChangeUserPasswordUpdateView(UpdateView):
    model = User
    form_class = ChangeUserPasswordForm
    template_name = 'user/user_form.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.set_password(obj.password)
        obj.save()
        return HttpResponseRedirect(reverse('users_list'))
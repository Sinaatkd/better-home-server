from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.views.generic import ListView, CreateView

from estate_module.models import Estate

from .user.forms import CreateUserForm

User = get_user_model()


def dashboard(request):
    all_users = User.objects.all()
    all_users_count = all_users.count()
    all_consultants_count = all_users.filter(is_consultant=True).count()
    all_estates_ads = Estate.objects.all().count()

    context = {
        'all_users_count': all_users_count,
        'all_consultants_count': all_consultants_count,
        'all_estates_ads': all_estates_ads,
    }
    return render(request, 'dashboard.html', context)


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

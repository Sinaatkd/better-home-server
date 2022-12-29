import psutil
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import get_user_model, authenticate, login

from estate_module.models import Estate


User = get_user_model()


def login_admin(request):
    if request.user.is_authenticated:
        next_url = request.GET.get('next')
        if next_url != '':
            return redirect(next_url)
        return redirect(reverse('dashboard'))
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            next_url = request.GET.get('next')
            if next_url != '':
                return redirect(next_url)
            return redirect(reverse('dashboard'))
    return render(request, 'login.html')


def dashboard(request):
    all_users = User.objects.all()
    all_users_count = all_users.count()
    all_consultants_count = all_users.filter(is_consultant=True).count()
    all_estates_ads = Estate.objects.all()
    memory_percent_usage = psutil.virtual_memory()[2]
    cpu_percent_usage = psutil.cpu_percent()
    latest_users = all_users.order_by('-id')[:10]
    latest_estates_ads = all_estates_ads.order_by('-id')[:10]

    context = {
        'all_users_count': all_users_count,
        'latest_users': latest_users,
        'all_consultants_count': all_consultants_count,
        'all_estates_ads': all_estates_ads.count(),
        'memory_percent_usage': memory_percent_usage,
        'cpu_percent_usage': cpu_percent_usage,
        'latest_estates_ads': latest_estates_ads,
    }
    return render(request, 'dashboard.html', context)


from django.shortcuts import render
from django.contrib.auth import get_user_model

from estate_module.models import Estate

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
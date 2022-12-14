from django.contrib.auth import get_user_model


User = get_user_model()


def update_consultants_quotas():
    consultants = User.objects.filter(is_consultant=True)
    for consultant in consultants:
        consultant.ad_monthly_quota = 10
        consultant.ladder_monthly_quota = 20
        consultant.special_ad_monthly_quota = 2
        consultant.save()

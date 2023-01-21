from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):    
    def handle(self, *args, **kwargs):
        consultants = User.objects.filter(is_consultant=True)
        for consultant in consultants:
            consultant.ad_monthly_quota = 10
            consultant.ladder_monthly_quota = 20
            consultant.special_ad_monthly_quota = 2
            consultant.save()
        self.stdout.write(self.style.SUCCESS(f'Quotas "{consultants.count()}" Consultants Updated'))
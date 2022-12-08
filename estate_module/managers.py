from datetime import datetime, timedelta

from django.db.models import Manager


class EstateManager(Manager):
    def create(self, **kwargs):
        kwargs['expire_time'] = datetime.now() + timedelta(days=30)
        return self.get_queryset().create(**kwargs)
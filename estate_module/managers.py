from django.db.models import Manager


class EstateManager(Manager):
    def active_estates(self):
        return self.get_queryset().filter(is_active=True, is_delete=False)
    
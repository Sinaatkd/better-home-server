from django.apps import AppConfig


class BaseModelModuleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base_model_module'

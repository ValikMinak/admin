from django.apps import AppConfig
from django.db.models.signals import post_save

from main_admin.models import Product
from main_admin.signals import post_save_product


class MainAdminConfig(AppConfig):
    name = 'main_admin'

    def ready(self):
        import signals

    # post_save.connect(post_save_product, sender=Product)

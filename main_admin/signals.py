from django.dispatch import receiver
from django.db.models.signals import post_save

from main_admin.models import Product


@receiver(post_save, sender=Product)
def post_save_product(sender, instance, created, *args, **kwargs):
    print("HEY", created)



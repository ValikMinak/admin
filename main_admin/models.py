from django.db import models

# signals
from django.dispatch import receiver
from django.db.models.signals import (
    post_save,
    post_delete, pre_save,
)
from django.utils.text import slugify

Rating = {
    ('b', 'Bad'),
    ('a', 'Average'),
    ('e', 'Excellent'),
}


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=100)
    published = models.BooleanField(default=False)
    # category = models.ForeignKey('Category', related_name='products', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(max_length=1, choices=Rating)

    def __str__(self):
        return self.name

    def show_descr(self):
        return self.description[:50]

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

# SIGNALS

# @receiver(pre_save, sender=Product)
# def product_post_save(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = slugify(instance.name)

# @receiver(post_save, sender=Product)
# def product_post_save(sender, instance, created, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = slugify(instance.name)
#         instance.save()

# @receiver(pre_save, sender=Product)
# def product_pre_save_receiver(sender, instance, *args, **kwargs):
#     print(instance.date, instance.id)
#
#
# @receiver(post_save, sender=Product)
# def product_post_save_receiver(sender, instance, created, *args, **kwargs):
#     if created:
#         print("Created", instance.name)
#     else:
#         print("Not created", instance.name)

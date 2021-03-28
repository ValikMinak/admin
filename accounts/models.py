from django.db import models


class Account(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.IntegerField()
    payment_token = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.email

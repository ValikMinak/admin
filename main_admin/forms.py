from django import forms
from django.contrib.admin.helpers import ActionForm


class ProductActionForm(ActionForm):
    slug = forms.CharField(max_length=200)

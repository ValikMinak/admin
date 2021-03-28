
from django import forms
from django.forms import CharField, Textarea

from items.models import Image


class ImageAdminForm(forms.BaseModelForm):
    image_urls = CharField(widget=Textarea, required=True)

    class Meta:
        model = Image
        fields = '__all__'

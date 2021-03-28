from django.contrib import admin
from django.core.validators import URLValidator
from django.forms import CharField, Textarea
from django.http import HttpResponseRedirect
from django import forms

from .models import Image


# def is_url_valid(url):
#     validate = URLValidator()
#     return validate(url)


# class AddImagesForm(forms.ModelForm):
#     image_urls = CharField(widget=Textarea, required=True, )
#
#     class Meta:
#         model = Image
#         fields = ('name', 'image_urls')
#
#     def clean_image_urls(self):
#         data = self.cleaned_data['image_urls']
#         is_url_valid(data)
#         return data
#

class ChangeImagesForm(forms.ModelForm):
    image_urls = CharField(widget=Textarea, required=True)

    class Meta:
        model = Image
        fields = ('name', 'image_urls')


class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_height', 'image_width')

    # def add_view(self, request, form_url='', extra_context=None):
    #     self.form = AddImagesForm
    #     return super().add_view(
    #         request, form_url, extra_context,
    #     )



    def change_view(self, request, object_id, form_url='', extra_context=None):
        self.form = ChangeImagesForm
        return super().change_view(
            request, object_id, form_url, extra_context,
        )
    # def get_urls(self):
    #     urls = super(ImageAdmin, self).get_urls()

    # custom_urls = [
    #     path('get_images/', self.get_images, name='change_slug'),
    # ]
    # return custom_urls + urls

    # def get_images(self, request):
    #     faker = Faker()
    #     urls = request.POST.get('image_urls').strip().split(",")
    #     for url in urls:
    #         image = Image()
    #         image.name = faker.first_name()
    #         image.save()
    #
    #         get_image.delay(url=url, pk=image.pk)
    #
    #     return HttpResponseRedirect('../')


admin.site.register(Image, ImageAdmin)

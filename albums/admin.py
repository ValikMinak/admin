import requests
from django.contrib import admin
from django import forms
from django.core.validators import URLValidator
from django.forms import CharField, Textarea
from django.shortcuts import redirect
from django.utils.safestring import mark_safe

from items.models import Image
from .tasks import get_image

from .models import Album


class ImagesInline(admin.TabularInline):
    model = Image
    fk_name = 'album'
    extra = 0
    readonly_fields = ('name', 'image_width', 'image_height', 'image_preview',)
    exclude = ('image',)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" alt="--" width=50px>')
        return '-'

    image_preview.short_description = 'Image'


class AdminAlbum(admin.ModelAdmin):
    list_display = ('name',)

    inlines = [
        ImagesInline,
    ]

    def add_view(self, request, form_url='', extra_context=None):
        self.form = AlbumAddForm
        return super().add_view(
            request, form_url, extra_context,
        )

    def change_view(self, request, object_id, form_url='', extra_context=None):
        self.form = AlbumChangeForm
        return super().change_view(
            request, object_id, form_url, extra_context,
        )

    def save_model(self, request, obj, form, change):
        super(AdminAlbum, self).save_model(request, obj, form, change)
        if request.POST and request.POST.get('image_urls'):
            urls = request.POST.get('image_urls').strip().split(",")
            count = 1
            for url in urls:
                image = Image()
                image.name = request.POST.get('name') + '-image-' + str(count)
                image.album = obj
                image.save()
                count += 1

                response = requests.get(url).content
                with open('media/photos/comic.png', 'wb') as f:
                    f.write(response)

                get_image.delay(url=url, pk=image.pk)

    def response_add(self, request, obj, post_url_continue=None):
        return redirect(f"/admin/albums/album/{obj.pk}/change/")

    def response_change(self, request, obj):
        return redirect(f"/admin/albums/album/{obj.pk}/change/")


def is_url_valid(url):
    validate = URLValidator()
    return validate(url)


class AlbumAddForm(forms.ModelForm):
    image_urls = CharField(widget=Textarea, required=True)

    class Meta:
        model = Album
        fields = ('name', 'image_urls')

    def clean_image_urls(self):
        data = self.cleaned_data['image_urls']
        is_url_valid(data)
        return data


class AlbumChangeForm(forms.ModelForm):
    image_urls = CharField(widget=Textarea, empty_value='https://picsum.photos/seed/picsum/200/300')

    class Meta:
        model = Album
        fields = ('name', 'image_urls')

    def clean_image_urls(self):
        data = self.cleaned_data['image_urls']
        is_url_valid(data)
        return data


admin.site.register(Album, AdminAlbum, )

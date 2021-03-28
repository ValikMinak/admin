from django.contrib import admin
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.urls import path

from .forms import ProductActionForm
from .models import Product

admin.site.site_header = 'Admin'


def change_rating(modeladmin, request, queryset):
    queryset.update(rating='e')


change_rating.short_description = 'Mark selected products as excellent'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    change_list_template = 'main_admin/admin/change_name_field.html'
    list_display = ('name', 'description', 'slug', 'published', 'rating',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('description',)
    list_filter = ('name',)

    def get_urls(self):
        urls = super(ProductAdmin, self).get_urls()
        custom_urls = [
            path('products/<str:name>/', self.change_name_field)
        ]
        return custom_urls + urls

    def change_name_field(self, request, name):
        print(request)
        self.model.objects.all().update(name=name)
        self.message_user(request, 'name changed')
        return HttpResponseRedirect("../")


# CHANGE SLUG HANDLE TEMPLATE ---------------------------------------------

# actions = ['change_slug']

# def get_urls(self):
#     urls = super(ProductAdmin, self).get_urls()
#
#     custom_urls = [
#         path('change_slug/', self.change_slug, name='change_slug'), ]
#     return custom_urls + urls

# def change_slug(self, request):
#     qs = self.model.objects.all()
#     for q in qs:
#         if q.slug == 'AAA':
#             q.slug = 'aaa'
#             q.save()
#         else:
#             q.slug = 'AAA'
#             q.save()

# self.message_user(request, 'Here some message')
# return HttpResponseRedirect('../')

# change_slug.short_description = 'Change_slug'


admin.site.unregister(Group)

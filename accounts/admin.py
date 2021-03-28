import json

from django.contrib import admin
from django.forms import CharField, Textarea

from accounts.models import Account
from django import forms


class AccountChangeForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('email', 'phone', 'payment_token',)

        fieldsets = (
            (None, {
                'fields': ('email', 'phone', 'payment_token',)
            }),
            ('Advanced options', {
                'classes': ('collapse',),
                'fields': ('first_name', 'last_name',),
            }),
        )


class AccountCreateForm(forms.ModelForm):
    card = CharField(widget=Textarea, required=True)

    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name', 'phone', 'card')


class AccountListForm(forms.ModelForm):
    image_urls = CharField(widget=Textarea, required=True)

    class Meta:
        model = Account
        fields = ('image_urls',)


class AccountAdmin(admin.ModelAdmin):
    form = AccountChangeForm

    def add_view(self, request, form_url='', extra_context=None):
        self.form = AccountCreateForm
        return super().add_view(
            request, form_url, extra_context=extra_context,
        )

    def change_view(self, request, object_id, form_url='', extra_context=None):
        self.form = AccountChangeForm
        return super().change_view(
            request, object_id, form_url, extra_context=extra_context,
        )

    def changelist_view(self, request, extra_context=None):
        self.form = AccountListForm
        return super().changelist_view(
            request, extra_context=extra_context,
        )


admin.site.register(Account, AccountAdmin)

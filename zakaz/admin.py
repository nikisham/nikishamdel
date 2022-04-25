from django.contrib import admin

from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from zakaz.models import Zakaz


class ZakazAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=CKEditorWidget(),label="Описание")

    class Meta:
        model = Zakaz
        fields = '__all__'


class ZakazAdmin(admin.ModelAdmin):
    form = ZakazAdminForm
    list_display = ('id', 'title', 'cost', 'cost_sale', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'id')

admin.site.register(Zakaz, ZakazAdmin)

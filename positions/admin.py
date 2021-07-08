from django.contrib import admin
from .models import Position
from django_summernote.admin import SummernoteModelAdmin


class SummerAdmin(SummernoteModelAdmin):
	summernote_fields = '__all__'


admin.site.register(Position, SummerAdmin)

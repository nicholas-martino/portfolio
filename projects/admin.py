from django.contrib import admin
from .models import Project
from django_summernote.admin import SummernoteModelAdmin


class SummerAdmin(SummernoteModelAdmin):
	summernote_fields = '__all__'


admin.site.register(Project, SummerAdmin)

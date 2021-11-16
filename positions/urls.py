from django.urls import path, include
from . import views

urlpatterns = [
	path("", views.positions, name="positions"),
	path('summernote/', include('django_summernote.urls')),
]

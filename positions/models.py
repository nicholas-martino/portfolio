from django.db import models
from django.utils import timezone
from datetime import datetime

class Position(models.Model):
	title = models.CharField(max_length=100)
	start_date = models.DateField()
	end_date = models.DateField(null=True, blank=True)
	institution = models.CharField(max_length=500)
	description = models.TextField(default=' ')
	hours = models.IntegerField(null=True, blank=True)
	education = models.BooleanField(default=False)

	def __str__(self):
		return f"{self.title}"

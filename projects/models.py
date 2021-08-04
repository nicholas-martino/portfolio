from django.db import models
from multiselectfield import MultiSelectField

TECHS = (
	('qgis', 'QGIS'),
	('python', 'Python'),
	('sql', 'SQL'),
	('grasshopper', 'Grasshopper'),
	('vray', 'V-Ray'),
	('lumion', 'Lumion'),
	('sketchup', 'SketchUp'),
	('csharp', 'C#'),
	('illustrator', 'Illustrator'),
	('photoshop', 'Photoshop'),
	('indesign', 'InDesign'),

)

class Project(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	detailed_description = models.TextField(null=True, blank=True)
	bottom_row = models.TextField(null=True, blank=True)
	date = models.DateField()
	image = models.FilePathField(path="static/img")
	technologies = MultiSelectField(choices=TECHS, default=(('python', 'Python')))
	code = models.URLField(null=True, blank=True)
	filter = models.CharField(default='filter-cd', max_length=30)
	publish = models.BooleanField(default=True)

	def __str__(self):
		return f"{self.title}"

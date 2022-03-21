from django.db import models
from multiselectfield import MultiSelectField

TECHS = (
	('qgis', 'QGIS'),
	('python', 'Python'),
	('js', 'JavaScript'),
	('vue_js', 'Vue'),
	('react_js', 'React'),
	('mapbox', 'Mapbox-GL'),
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

FILTERS = (
	('filter-ds', 'Data Science'),
	('filter-gd', 'Generative Design'),
	('filter-wd', 'Web Development')
)


class Project(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	detailed_description = models.TextField(null=True, blank=True)
	date = models.DateField()
	image = models.FilePathField(path="static/img")
	technologies = MultiSelectField(choices=TECHS, default=(('python', 'Python')))
	link = models.URLField(null=True, blank=True)
	code = models.URLField(null=True, blank=True)
	filter = models.CharField(default='filter-gd', max_length=30)
	publish = models.BooleanField(default=True)
	model = models.URLField(null=True, blank=True)

	def __str__(self):
		return f"{self.title}"

from projects.models import Project

SHIFT = 1

objects = Project.objects.all().order_by('order')
if SHIFT > 0: objects = reversed(objects)
for project in objects:
	project.order = project.order + SHIFT
	project.save()

from django.contrib import admin
from . import models


admin.site.register(models.User)
admin.site.register(models.Coords)
admin.site.register(models.DifficultyLevel)
admin.site.register(models.ModerationStatus)
admin.site.register(models.Pereval)
admin.site.register(models.PerevalImages)
admin.site.register(models.PerevalAreas)
admin.site.register(models.ActivitiesTypes)

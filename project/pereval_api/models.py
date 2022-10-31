from django.db import models


class User(models.Model):
    email = models.EmailField(primary_key=True)
    phone = models.BigIntegerField()
    name = models.TextField()

    class Meta:
        db_table = 'pereval_users'


class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()

    class Meta:
        db_table = 'preval_coordinates'


class DifficultyLevel(models.Model):
    name = models.TextField(primary_key=True)

    class Meta:
        db_table = 'pereval_level'


class ModerationStatus(models.Model):
    name = models.TextField(primary_key=True)

    class Meta:
        db_table = 'moderation_status'


class Pereval(models.Model):
    beautyTitle = models.TextField()
    title = models.TextField()
    other_titles = models.TextField()
    connect = models.TextField(null=True)
    add_time = models.DateTimeField()
    coord_id = models.OneToOneField(Coords, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    level_winter = models.ForeignKey(DifficultyLevel, on_delete=models.CASCADE, related_name='winter_level')
    level_summer = models.ForeignKey(DifficultyLevel, on_delete=models.CASCADE, related_name='summer_level')
    level_autumn = models.ForeignKey(DifficultyLevel, on_delete=models.CASCADE, related_name='autumn_level')
    level_spring = models.ForeignKey(DifficultyLevel, on_delete=models.CASCADE, related_name='spring_level')
    status = models.ForeignKey(ModerationStatus, on_delete=models.CASCADE, default='new')

    class Meta:
        db_table = 'pereval_added'


class PerevalImages(models.Model):
    title = models.TextField()
    date_added = models.DateTimeField(auto_now=True)
    image = models.BinaryField
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE)

    class Meta:
        db_table = 'pereval_images'


class PerevalAreas(models.Model):
    id_parent = models.BigIntegerField()
    title = models.TextField()

    class Meta:
        db_table = 'pereval_areas'


class ActivitiesTypes(models.Model):
    title = models.TextField()

    class Meta:
        db_table = 'spr_activities_types'

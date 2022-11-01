from . import models
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('email', 'phone', 'name',)


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Coords
        fields = ('id', 'latitude', 'longitude', 'height',)


class DifficultyLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DifficultyLevel
        fields = ('name',)


class ModerationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModerationStatus
        fields = ('name',)


class PerevalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pereval
        fields = (
            'id',
            'beautyTitle',
            'title',
            'other_titles',
            'connect',
            'add_time',
            'coord_id',
            'user',
            'level_winter',
            'level_summer',
            'level_autumn',
            'level_spring',
            'status',
        )


class PerevalImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PerevalImages
        fields = ('id', 'title', 'date_added', 'image', 'pereval',)


class PerevalAreasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PerevalAreas
        fields = ('id', 'id_parent', 'title',)


class ActivitiesTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ActivitiesTypes
        fields = ('id', 'title',)

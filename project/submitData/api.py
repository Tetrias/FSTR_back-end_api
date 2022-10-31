from rest_framework.generics import ListAPIView, ListCreateAPIView
from . import serializers
from . import models


class UserListAPIView(ListAPIView, ListCreateAPIView):
    """Список пользователей"""
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        return models.User.objects.all()


class CoordsListAPIView(ListAPIView, ListCreateAPIView):
    """Список координат"""
    serializer_class = serializers.CoordsSerializer

    def get_queryset(self):
        return models.Coords.objects.all()


class LevelListAPIView(ListAPIView, ListCreateAPIView):
    """Список уровней сложности перевала"""
    serializer_class = serializers.DifficultyLevelSerializer

    def get_queryset(self):
        return models.DifficultyLevel.objects.all()


class StatusListAPIView(ListAPIView, ListCreateAPIView):
    """Список статуса модерации добавляемых перевалов"""
    serializer_class = serializers.ModerationStatusSerializer

    def get_queryset(self):
        return models.ModerationStatus.objects.all()


class PerevalListAPIView(ListAPIView, ListCreateAPIView):
    """Список добавленных перевалов"""
    serializer_class = serializers.PerevalSerializer

    def get_queryset(self):
        return models.Pereval.objects.all()


class ImagesListAPIView(ListAPIView, ListCreateAPIView):
    """Список изображений перевалов"""
    serializer_class = serializers.PerevalImagesSerializer

    def get_queryset(self):
        return models.PerevalImages.objects.all()


class AreasListAPIView(ListAPIView, ListCreateAPIView):
    """Список мест перевалов"""
    serializer_class = serializers.PerevalAreasSerializer

    def get_queryset(self):
        return models.PerevalAreas.objects.all()


class ActivitiesListAPIView(ListAPIView, ListCreateAPIView):
    """Список типов активности"""
    serializer_class = serializers.ActivitiesTypesSerializer

    def get_queryset(self):
        return models.ActivitiesTypes.objects.all()

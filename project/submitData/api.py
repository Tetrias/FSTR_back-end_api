from rest_framework.generics import ListAPIView, ListCreateAPIView, UpdateAPIView, RetrieveAPIView
from . import serializers
from . import models


class UserListAPIView(ListAPIView, ListCreateAPIView):
    """Список пользователей и их создание"""
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        return models.User.objects.all()


class CoordsListAPIView(ListAPIView, ListCreateAPIView):
    """Список координат и их создание"""
    serializer_class = serializers.CoordsSerializer

    def get_queryset(self):
        return models.Coords.objects.all()


class LevelListAPIView(ListAPIView, ListCreateAPIView):
    """Список уровней сложности перевала и их создание"""
    serializer_class = serializers.DifficultyLevelSerializer

    def get_queryset(self):
        return models.DifficultyLevel.objects.all()


class StatusListAPIView(ListAPIView, ListCreateAPIView):
    """Список статуса модерации добавляемых перевалов и их создание"""
    serializer_class = serializers.ModerationStatusSerializer

    def get_queryset(self):
        return models.ModerationStatus.objects.all()


class PerevalListAPIView(ListAPIView, ListCreateAPIView):
    """Список добавленных перевалов и их создание"""
    serializer_class = serializers.PerevalSerializer

    def get_queryset(self):
        return models.Pereval.objects.all()


class PerevalUpdateAPIView(RetrieveAPIView, UpdateAPIView):
    """Просмотр отдельной записи перевала и её редактирование"""
    serializer_class = serializers.PerevalSerializer

    def get_queryset(self):
        return models.Pereval.objects.all().filter(pk=self.kwargs['pk'])


class UserPerevalListAPIView(ListAPIView):
    """Список всех записей добавленных определенным пользователем."""
    serializer_class = serializers.PerevalSerializer

    def get_queryset(self):
        return models.Pereval.objects.all().filter(user=self.kwargs['pk'])


class ImagesListAPIView(ListAPIView, ListCreateAPIView):
    """Список изображений перевалов и их создание"""
    serializer_class = serializers.PerevalImagesSerializer

    def get_queryset(self):
        return models.PerevalImages.objects.all()


class AreasListAPIView(ListAPIView, ListCreateAPIView):
    """Список мест перевалов и их создание"""
    serializer_class = serializers.PerevalAreasSerializer

    def get_queryset(self):
        return models.PerevalAreas.objects.all()


class ActivitiesListAPIView(ListAPIView, ListCreateAPIView):
    """Список типов активности и их создание"""
    serializer_class = serializers.ActivitiesTypesSerializer

    def get_queryset(self):
        return models.ActivitiesTypes.objects.all()

from rest_framework.generics import ListAPIView, ListCreateAPIView, GenericAPIView
from rest_framework import mixins
from rest_framework.response import Response

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


class PerevalUpdateAPIView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericAPIView):
    """Просмотр отдельной записи перевала и её редактирование"""
    queryset = models.Pereval.objects.all()
    serializer_class = serializers.PerevalSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        status_new = models.ModerationStatus.objects.get(name='new')
        pereval = self.queryset.get(pk=self.kwargs['pk'])

        if pereval.status == status_new:
            return self.update(request, *args, **kwargs)
        else:
            return Response('Редактирование запрещено, запись уже была отправлена на модерацию.')


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

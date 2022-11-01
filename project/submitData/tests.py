from django.urls import reverse
from rest_framework.test import APITestCase

from . import serializers
from . import models


class SubmitDataAPITextCase(APITestCase):
    def test_pereval_added(self):
        # Создания уровней сложности.
        lvl1 = models.DifficultyLevel.objects.create(
            name='1А',
        )
        lvl2 = models.DifficultyLevel.objects.create(
            name='2А',
        )
        url = reverse('api_level')
        response = self.client.get(url)
        serializers_data = serializers.DifficultyLevelSerializer([lvl1, lvl2], many=True).data
        self.assertEqual(serializers_data, response.data)

        # Создание статуса модерации.
        status1 = models.ModerationStatus.objects.create(
            name='new',
        )
        status2 = models.ModerationStatus.objects.create(
            name='pending',
        )
        url = reverse('api_status')
        response = self.client.get(url)
        serializers_data = serializers.ModerationStatusSerializer([status1, status2], many=True).data
        self.assertEqual(serializers_data, response.data)

        # Создание пользователя.
        user1 = models.User.objects.create(
            email='test_1@example.com',
            phone=88005553535,
            name='Иванов Иван Иванович',
        )
        user2 = models.User.objects.create(
            email='test_2@example.com',
            phone=88095553535,
            name='Иванов Иван Петрович',
        )
        url = reverse('api_user')
        response = self.client.get(url)
        serializers_data = serializers.UserSerializer([user1, user2], many=True).data
        self.assertEqual(serializers_data, response.data)

        # Создание координат.
        coord1 = models.Coords.objects.create(
            latitude=45.3842,
            longitude=7.1525,
            height=1200,
        )
        coord2 = models.Coords.objects.create(
            latitude=46.3842,
            longitude=8.1525,
            height=1201,
        )
        url = reverse('api_coords')
        response = self.client.get(url)
        serializers_data = serializers.CoordsSerializer([coord1, coord2], many=True).data
        self.assertEqual(serializers_data, response.data)

        # Создание перевалов.
        pereval1 = models.Pereval.objects.create(
            beautyTitle="пер. ",
            title="Пхия",
            other_titles="Триев",
            connect="",
            add_time="2022-11-01T18:21:00Z",
            coord=coord1,
            user=user1,
            level_winter=lvl1,
            level_spring=lvl1,
        )
        pereval2 = models.Pereval.objects.create(
            beautyTitle="пер. ",
            title="Пхия",
            other_titles="Триев",
            connect="",
            add_time="2021-11-01T18:21:00Z",
            coord=coord2,
            user=user2,
            level_summer=lvl2,
            level_autumn=lvl2,
        )
        url = reverse('api_pereval')
        response = self.client.get(url)
        serializers_data = serializers.PerevalSerializer([pereval1, pereval2], many=True).data
        self.assertEqual(serializers_data, response.data)

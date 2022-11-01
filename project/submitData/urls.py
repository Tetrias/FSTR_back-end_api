from django.urls import path
from . import api

urlpatterns = [
    path('user', api.UserListAPIView.as_view(), name='api_user'),
    path('user__email=<str:pk>', api.UserPerevalListAPIView.as_view(), name='user_pereval_list'),
    path('coord', api.CoordsListAPIView.as_view(), name='api_coords'),
    path('level', api.LevelListAPIView.as_view(), name='api_level'),
    path('status', api.StatusListAPIView.as_view(), name='api_status'),
    path('pereval', api.PerevalListAPIView.as_view(), name='api_pereval'),
    path('<int:pk>', api.PerevalUpdateAPIView.as_view(), name='pereval_detail'),
    path('images', api.ImagesListAPIView.as_view(), name='api_images'),
    path('areas', api.AreasListAPIView.as_view(), name='api_areas'),
    path('activities', api.ActivitiesListAPIView.as_view(), name='api_activities'),
]

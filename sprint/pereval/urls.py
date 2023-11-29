from django.urls import path
from .views import PerevalViewSet


urlpatterns = [
    path('pereval/', PerevalViewSet.as_view({'get': 'list'})),
]



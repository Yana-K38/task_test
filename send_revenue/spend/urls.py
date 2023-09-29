from django.urls import path

from .views import SpendAPIView

urlpatterns = [
    path("spend-statistic/", SpendAPIView.as_view(), name="spend-statistic"),
]

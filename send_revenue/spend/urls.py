from .views import SpendAPIView
from django.urls import path


urlpatterns = [
    path('spend-statistic/', SpendAPIView.as_view(), name='spend-statistic'),
]
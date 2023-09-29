from .views import RevenueAPIView
from django.urls import path


urlpatterns = [
    path('revenue-statistic/', RevenueAPIView.as_view(), name='revenue-statistic'),
]

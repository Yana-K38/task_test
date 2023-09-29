from django.urls import path

from .views import RevenueAPIView

urlpatterns = [
    path("revenue-statistic/", RevenueAPIView.as_view(), name="revenue-statistic"),
]

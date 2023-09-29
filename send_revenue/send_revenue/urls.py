from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("spend/", include("spend.urls")),
    path("revenue/", include("revenue.urls")),
]

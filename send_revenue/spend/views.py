from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SpendStatistic
from revenue.models import RevenueStatistic
from django.db.models import Sum 


class SpendAPIView(APIView):
    def get(self, request):
        queryset = SpendStatistic.objects.values('name', 'date').annotate(
            total_spend = Sum('spend'),
            total_impressions = Sum('impressions'),
            total_clicks = Sum('clicks'),
            total_conversion = Sum('conversion'),
            total_revenue=Sum('revenue__revenue'),
        )
        
        return Response({'data': list(queryset)}, status=status.HTTP_200_OK)
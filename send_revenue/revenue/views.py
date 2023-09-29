from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import RevenueStatistic
from spend.models import SpendStatistic
from django.db.models import Sum 


class RevenueAPIView(APIView):
    def get(self, request):
        queryset = RevenueStatistic.objects.values('name', 'date').annotate(
            total_revenue = Sum('revenue'),
            total_spend = Sum('spend__spend'),
            total_impressions = Sum('spend__impressions'),
            total_clicks = Sum('spend__clicks'),
            total_conversion = Sum('spend__conversion'),
        )
        
        return Response({'data': list(queryset)})
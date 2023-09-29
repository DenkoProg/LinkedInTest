from django.db.models import Subquery, OuterRef
from spend.models import SpendStatistic
from rest_framework.decorators import api_view
from rest_framework.response import Response
from revenue.models import RevenueStatistic
from django.db.models import Sum, F
from django.db import models


@api_view(['GET'])
def spend_statistic_view(request):
    subquery = RevenueStatistic.objects.filter(
        spend=OuterRef('pk')
    ).annotate(total_revenue=Sum('revenue')).values('total_revenue')

    queryset = SpendStatistic.objects.annotate(
        total_spend=Sum('spend'),
        total_impressions=Sum('impressions'),
        total_clicks=Sum('clicks'),
        total_conversion=Sum('conversion'),
        total_revenue=Subquery(subquery, output_field=models.DecimalField())
    ).order_by('name', 'date')

    results = []

    for obj in queryset:
        results.append({
            'name': obj.name,
            'date': obj.date,
            'total_spend': obj.total_spend,
            'total_impressions': obj.total_impressions,
            'total_clicks': obj.total_clicks,
            'total_conversion': obj.total_conversion,
            'total_revenue': obj.total_revenue,
        })

    return Response(results)




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
    ).values('revenue')

    queryset = SpendStatistic.objects.annotate(
        total_spend=Sum('spend'),
        total_impressions=Sum('impressions'),
        total_clicks=Sum('clicks'),
        total_conversion=Sum('conversion'),
        revenue=Subquery(subquery, output_field=models.DecimalField())
    ).order_by('name', 'date')

    return Response(queryset)

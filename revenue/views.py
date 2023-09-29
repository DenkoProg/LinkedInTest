from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum
from .models import RevenueStatistic

@api_view(['GET'])
def revenue_statistic_view(request):
    queryset = RevenueStatistic.objects.all().annotate(
        total_revenue=Sum('revenue')
    ).order_by('name', 'date')

    results = []

    for obj in queryset:
        results.append({
            'name': obj.name,
            'date': obj.date,
            'total_revenue': obj.total_revenue,
            'spend': obj.spend.spend if obj.spend else None,
            'impressions': obj.spend.impressions if obj.spend else None,
            'clicks': obj.spend.clicks if obj.spend else None,
            'conversion': obj.spend.conversion if obj.spend else None,
        })

    return Response(results)

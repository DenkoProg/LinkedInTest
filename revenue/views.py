from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum
from .models import RevenueStatistic

@api_view(['GET'])
def revenue_statistic_view(request):
    queryset = RevenueStatistic.objects.values('name', 'date', 'spend__spend', 'spend__impressions', 'spend__clicks', 'spend__conversion').annotate(
        total_revenue=Sum('revenue')
    ).order_by('name', 'date')

    results = []

    for obj in queryset:
        results.append({
            'name': obj['name'],
            'date': obj['date'],
            'total_revenue': obj['total_revenue'],
            'spend': obj['spend__spend'],
            'impressions': obj['spend__impressions'],
            'clicks': obj['spend__clicks'],
            'conversion': obj['spend__conversion'],
        })

    return Response(results)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum, F
from .models import RevenueStatistic


@api_view(['GET'])
def revenue_statistic_view(request):
    queryset = RevenueStatistic.objects.annotate(
        total_revenue=Sum('revenue'),
        spend_value=F('spend__spend'),
        impressions=F('spend__impressions'),
        clicks=F('spend__clicks'),
        conversion=F('spend__conversion')
    ).order_by('name', 'date')

    return Response(queryset)

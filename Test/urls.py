from django.contrib import admin
from django.urls import path
from revenue import views as RevenueViews
from spend import views as SpendViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('revenue/', RevenueViews.revenue_statistic_view, name='revenue-statistic'),
    path('spend/', SpendViews.spend_statistic_view, name='spend-statistic'),
]

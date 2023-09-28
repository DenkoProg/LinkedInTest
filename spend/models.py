from django.db import models


class SpendStatistic(models.Model):
   name = models.CharField(max_length=255)
   date = models.DateField()
   spend = models.DecimalField(max_digits=10, decimal_places=2, default=0)
   impressions = models.DecimalField(max_digits=10, decimal_places=2, default=0)
   clicks = models.DecimalField(max_digits=10, decimal_places=2, default=0)
   conversion = models.DecimalField(max_digits=10, decimal_places=2, default=0)
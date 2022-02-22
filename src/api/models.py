from django.db import models
from datetime import datetime
# Create your models here.


class SKU(models.Model):
    sku = models.CharField(max_length=100)

    class Meta:
        db_table = "sku"

    def __str__(self):
        return self.sku


class RetailerBranch(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "retailer_branch"

    def __str__(self):
        return self.name


class Schedule(models.Model):
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    date = models.DateTimeField()
    frequency = models.IntegerField()

    class Meta:
        db_table = "schedule"

    def __str__(self):
        return f'{self.id}'


class SurveyResponse(models.Model):
    STATUS_CHOICES = (
        ('approved', 'Approved'),
        ('pending', 'Pending'),
        ('declined', 'Declined')
    )

    schedule = models.ForeignKey(
        Schedule,
        null=True,
        on_delete=models.CASCADE
    )
    retailer_branch = models.ForeignKey(
        RetailerBranch,
        null=True,
        on_delete=models.CASCADE
    )
    status = models.CharField(
        max_length=8, choices=STATUS_CHOICES, default='pending')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True),
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True),
    is_completed = models.BooleanField(default=False)

    def _str_(self):
        return str(self.id)

    def mark_completed(self):
        self.is_completed = True
        self.updated = datetime.now()
        self.save(update_fields=['is_completed', 'updated'])


class SKUAvailability(models.Model):
    survey_response = models.ForeignKey(
        SurveyResponse, on_delete=models.CASCADE)
    sku = models.ForeignKey(SKU, on_delete=models.CASCADE)
    is_available = models.BooleanField()

    def _str_(self):
        return str(self.id)

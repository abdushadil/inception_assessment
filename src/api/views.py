from django.shortcuts import render
from api.models import SKUAvailability
from django.db.models.functions import TruncMonth
from django.db.models import Count
from django.views.generic import TemplateView
from django.http import JsonResponse
# Create your views here.


class AuditReportUseCase():
    def _factory(self):
        return list(SKUAvailability.objects.filter(survey_response__status='approved').annotate(
            month=TruncMonth('survey_response__schedule__date')
        ).values(
            'month'
        ).annotate(
            audit=Count('survey_response', distinct=True)
        ).values('month', 'audit'))


"""
Equivelant MYSQL Raw Query

SELECT api_skuavailability.id, (SELECT date FROM schedule WHERE schedule.id=api_surveyresponse.schedule_id) AS month, (SELECT DISTINCT COUNT(*) FROM api_surveyresponse) AS audit FROM api_skuavailability
LEFT JOIN api_surveyresponse
ON api_skuavailability.survey_response_id = api_surveyresponse.id;
"""

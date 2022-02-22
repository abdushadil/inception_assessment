from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from api.views import approved_surveys_sku

urlpatterns = [
    path('approved_surveys_sku/', approved_surveys_sku),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

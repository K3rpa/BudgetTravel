from django.urls import path
from .views import ChicagoModelViews

app_name = "ChicagoModel"

urlpatterns = [
    path('ChicagoModel', ChicagoModelViews.as_view()),
]
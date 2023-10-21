from django.urls import path
from .views import PortlandModelViews

app_name = "PortlandModel"

urlpatterns = [
    path('PortlandModel', PortlandModelViews.as_view()),
]
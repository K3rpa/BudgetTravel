from django.urls import path
from .views import AustinModelViews

app_name = "AustinModel"

urlpatterns = [
    path('AustinModel', AustinModelViews.as_view()),
]
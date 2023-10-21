from django.urls import path
from .views import TourismViews

app_name = "toursism"

urlpatterns = [
    path('Tourism', TourismViews.as_view()),
]
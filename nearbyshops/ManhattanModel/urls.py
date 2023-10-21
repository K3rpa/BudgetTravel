from django.urls import path
from .views import ManhattanModelViews

app_name = "ManhattanModel"

urlpatterns = [
    path('ManhhatanModel', ManhattanModelViews.as_view()),
]
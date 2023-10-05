from django.urls import path
from .views import RestaurantViews

app_name = "restaurants"

urlpatterns = [
    path('restaurants', RestaurantViews.as_view()),
]
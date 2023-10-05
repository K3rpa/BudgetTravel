from django.urls import path
from .views import ShopViews


app_name = "shops"

urlpatterns = [
    path('shops', ShopViews.as_view()),
]
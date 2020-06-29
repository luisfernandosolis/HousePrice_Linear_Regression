from django.urls import path
from .views import ModelRegression

urlpatterns = [
    path('',ModelRegression.as_view(),name="model")
]
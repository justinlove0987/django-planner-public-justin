from django.urls import path
from . import views

urlpatterns = [
    path("", views.analytics, name="analytics"),
    path("update_chart", views.update_chart, name="update_chart")
]

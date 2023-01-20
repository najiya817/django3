from django.urls import path
from .views import AddMark

urlpatterns=[
    path('addmrk/',AddMark.as_view(),name="markk")
]
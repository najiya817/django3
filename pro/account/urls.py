from django.urls import path
from .views import LogView, RegView

urlpatterns=[
    path('reg/',RegView.as_view(),name='reg'),
    path('log/',LogView.as_view(),name="log")
    


]
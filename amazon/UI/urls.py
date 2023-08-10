from django.urls import path
from UI import views

urlpatterns = [
    path('web', views.website),
    path('UI', views.web),
]

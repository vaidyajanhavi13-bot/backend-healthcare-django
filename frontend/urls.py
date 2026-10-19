from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("patients/", views.patients_page, name="patients-page"),
    path("doctors/", views.doctors_page, name="doctors-page"),
    path("mappings/", views.mappings_page, name="mappings-page"),
]
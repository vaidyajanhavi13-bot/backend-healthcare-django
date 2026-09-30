from django.urls import path
from .views import MappingListCreateView, MappingPatientView

urlpatterns = [
    path(
        "",
        MappingListCreateView.as_view(),
        name="mapping-list-create"
    ),
    path(
        "<int:patient_id>/",
        MappingPatientView.as_view(),
        name="mapping-patient"
    ),
]
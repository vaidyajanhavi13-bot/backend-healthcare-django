from patients.models import Patient
from doctors.models import Doctor
from mappings.models import PatientDoctorMapping

from django.shortcuts import render

def dashboard(request):
    context = {
        "patient_count": Patient.objects.count(),
        "doctor_count": Doctor.objects.count(),
        "mapping_count": PatientDoctorMapping.objects.count(),
    }
    return render(request, "frontend/dashboard.html", context)

def patients_page(request):
    patients = Patient.objects.all()
    return render(
        request,
        "frontend/patients.html",
        {"patients": patients}
    )

def doctors_page(request):
    return render(request, "frontend/doctors.html")

def mappings_page(request):
    return render(request, "frontend/mappings.html")
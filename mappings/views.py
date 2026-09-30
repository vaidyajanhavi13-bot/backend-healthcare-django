from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer


class MappingListCreateView(generics.ListCreateAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PatientDoctorMapping.objects.filter(
            patient__created_by=self.request.user
        )

    def perform_create(self, serializer):
        patient = serializer.validated_data["patient"]

        if patient.created_by != self.request.user:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied(
                "You can only assign doctors to your own patients."
            )

        serializer.save()


class MappingPatientView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, patient_id):
        mappings = PatientDoctorMapping.objects.filter(
            patient_id=patient_id,
            patient__created_by=request.user
        )

        serializer = PatientDoctorMappingSerializer(mappings, many=True)
        return Response(serializer.data)

    def delete(self, request, patient_id):
        mapping = get_object_or_404(
            PatientDoctorMapping,
            id=patient_id,
            patient__created_by=request.user
        )

        mapping.delete()

        return Response(
            {"message": "Mapping deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
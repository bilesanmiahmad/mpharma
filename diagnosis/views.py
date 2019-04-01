from django.shortcuts import render, get_object_or_404
from rest_framework import views, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from diagnosis import serializers
from diagnosis import models

# Create your views here.
class CategoryViewset(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class DiagnosisViewset(viewsets.ModelViewSet):
    queryset = models.Diagnosis.objects.all()
    serializer_class = serializers.DiagnosisInputSerializer

    def list(self, request):
        records = models.Diagnosis.objects.all()
        serializer = serializers.DiagnosisOutputSerializer(records, many=True)
        return Response(
            {
                'results': serializer.data
            },
            status=status.HTTP_200_OK
        )

    def retrieve(self, request, pk=None):
        queryset = models.Diagnosis.objects.all()
        record = get_object_or_404(queryset, pk=pk)
        serializer = serializers.DiagnosisOutputSerializer(record)
        return Response(
            {
                'results': serializer.data
            },
            status=status.HTTP_200_OK
        )

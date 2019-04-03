from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.serializers import ValidationError
from rest_framework.test import APIClient, APIRequestFactory
from diagnosis.models import Diagnosis, Category
from diagnosis.serializers import DiagnosisInputSerializer, DiagnosisOutputSerializer
from diagnosis.views import DiagnosisViewset as dv

client = Client()

class TestDiagnosisViewset(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = dv.as_view({'get': 'list'})
        self.uri = '/diagnosis/'
        self.retrieve_view = dv.as_view({'get': 'retrieve'})
        self.retrieve_uri = '/diagnosis/4/'
        category = Category.objects.create(
            code='J6',
            title='Blood Pressure'
        )
        diagnosis = Diagnosis.objects.create(
            code=4876,
            category=category,
            description='Hypertensive Blood Pressure'
        )
    
    def testAllDiagnosis(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEquals(response.status_code, 200)

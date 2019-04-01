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
        self.one_view = dv.as_view({'get': 'retrieve'})
        self.one_uri = '/diagnosis/4/'
        category = Category.objects.create(
            code='J6',
            title='Blood Pressure'
        )
        diagnosis = Diagnosis.objects.create(
            code=4876,
            category=category,
            description='Hypertensive Blood Pressure'
        )
        print(diagnosis.id)
    
    def testAllDiagnosis(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        print(response.data)
        self.assertEquals(response.status_code, 200)
    
    def testOneDiagnosis(self):
        request = self.factory.get('/diagnosis/4')
        print(request.build_absolute_uri())
        response = self.one_view(request)
        print(response)
        self.assertEquals(response.status_code, 200)
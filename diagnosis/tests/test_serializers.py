from django.test import TestCase
from rest_framework.serializers import ValidationError
from diagnosis.models import Diagnosis, Category
from diagnosis.serializers import DiagnosisInputSerializer

class TestDiagnosisSerializers(TestCase):

    def setUp(self):
        category = Category.objects.create(
            code='E1',
            title='Malaria'
        )
        diagnosis = Diagnosis(
            code=3450, 
            category=category, 
            description='Malaria Parasites'
        )
        diagnosis.save()

    def test_validate_category(self):
        with self.assertRaises(ValidationError):
            diagnosis = DiagnosisInputSerializer.validate(
                self,
                data={'code': 3450, 'category': 5, 'title': 'Malaria Parasites'}
            )

from django.test import TestCase
from diagnosis.models import Diagnosis, Category

class CategoryTest(TestCase):

    def setUp(self):
        Category.objects.create(code='A1', title='Malaria')
        Category.objects.create(code='B1', title='Cholera')
        Category.objects.create(code='C1', title='Typhoid')
    
    def test_create_category(self):
        category = Category.objects.create(
            code='D1', title='Chicken Pox')
        self.assertEquals(category.__str__(), category.code)

class DiagnosisTest(TestCase):

    def setUp(self):
        category = Category.objects.create(code='A1', title='Malaria')
        diagnosis = Diagnosis.objects.create(
            code='4576',
            category=category,
            description='Polio diagnosis'
        )

    def test_create_diagnosis(self):
        category = Category.objects.create(code='E1', title='Polio')
        diagnosis = Diagnosis.objects.create(
            code='4576',
            category=category,
            description='Chronic Malaria'
        )
        self.assertEquals(diagnosis.full_code, 'E14576')
        self.assertEquals(diagnosis.__str__(), diagnosis.code)
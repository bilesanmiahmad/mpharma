from rest_framework import serializers
from diagnosis.models import Category, Diagnosis


class CategorySerializer(serializers.ModelSerializer): 
    class Meta:
        model = Category
        fields = ['id', 'code', 'title']


class DiagnosisInputSerializer(serializers.ModelSerializer):
    """
        Serializer for receiving new diagnosis data
    """
    def validate(self, data):
        try:
            category = Category.objects.get(code=data.get('category', None))
        except Category.DoesNotExist:
            raise serializers.ValidationError('Category Does Not Exist')

        category_code = category.code
        diagnosis_code = data.get('code', '')
        full_code = '{}{}'.format(category_code, diagnosis_code)
        try:
            record = Diagnosis.objects.get(full_code=full_code)
            if record:
                raise serializers.ValidationError(
                    'Diagnosis Code already exists.'
                    'Please use a different code')
        except Diagnosis.DoesNotExist:
            return data

    class Meta:
        model = Diagnosis
        fields = [
            'code', 'category', 'description',]


class DiagnosisOutputSerializer(serializers.ModelSerializer):
    """
        Serializer for displaying diagnosis data
    """
    category = CategorySerializer()
    
    class Meta:
        model = Diagnosis
        fields = [
            'id', 'code', 'category', 'description', 
            'full_code']
        read_only_fields = ('full_code',)
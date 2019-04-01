from django.db import models

# Create your models here.

class Category(models.Model):
    code = models.CharField(
        'Category Code',
        max_length=2,
        unique=True
    )
    title = models.CharField(
        'Category Title',
        max_length=50,
        blank=True, null=True
    )
    created = models.DateTimeField(
        'Created On',
        auto_now_add=True
    )
    updated = models.DateTimeField(
        'Updated On',
        auto_now=True
    )

    def __str__(self):
        return self.code


class Diagnosis(models.Model):
    code = models.IntegerField(
        'Diagnosis Code',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='categories'
    )
    description = models.CharField(
        'Description',
        max_length=70,
        blank=True, null=True
    )
    created = models.DateTimeField(
        'Created On',
        auto_now_add=True
    )
    updated = models.DateTimeField(
        'Updated On',
        auto_now=True
    )
    full_code = models.CharField(
        'Full Code',
        max_length=10,
        unique=True
    )

    def save(self, *args, **kwargs):
        self.full_code = self.category.code + str(self.code)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.code)
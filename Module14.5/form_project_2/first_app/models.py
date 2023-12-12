from django.db import models

# Create your models here.

class StudentModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    address = models.TextField()
    father_name = models.TextField(default='Tarek Uddin')
    date_field = models.DateField(null=True)
    big_integer_field = models.BigIntegerField( null=True)
    binary_field = models.BinaryField(null = True)
    # update code 12-12-2023
    time_field = models.TimeField(null=True)
    url_field = models.URLField(null=True)
    uuid_field = models.UUIDField(null=True)
    slug_field = models.SlugField(null=True)
    positive_integer_field = models.PositiveIntegerField(null=True)



    def __str__(self):
        return f'Roll: {self.roll} - {self.name}'

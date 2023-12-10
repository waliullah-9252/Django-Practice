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


    def __str__(self):
        return f'Roll: {self.roll} - {self.name}'

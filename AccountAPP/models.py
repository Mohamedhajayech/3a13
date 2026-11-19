from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator,MaxLengthValidator,RegexValidator
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.
class User (AbstractUser):
    pass
number_validaor=RegexValidator(
    regex=r'^\d{8}$',
    message="le numero doit contenir 8 chiffres"
    )
    def brith_date_validator(d):

        if d >= timezone.localdate():
            raise ValidationError("La date de naissance doit être antérieure à la date actuelle.")

class Doctor (User):
    license_number = models.CharField(max_length=6, unique=True, validators=[MinLengthValidator(6), MaxLengthValidator(6)])
    phone=models.CharField(max_length=8, validators=number_validaor)
    specialty=models.ManyToManyField(AccountApp.specialty, related_name='doctors')
    

class Patient (User):
    national_id=models.CharField(max_length=8, unique=True, validators=number_validaor)
    phone=models.CharField(max_length=8, validators=[number_validaor])
    birth_date= models.DateField(validators=[birth_date_validator])
class Specialty(models.Model):
    name=models.CharField(max_length=50, unique=True)
    description=models.TextField()

from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Sex(models.Model):
    # male or female
    title = models.CharField(max_length=10)
    def __str__(self):
        return self.title

class ChestPain(models.Model):
    # typical angina, atypical angina, non-anginal pain, asymptomatic
    title = models.CharField(max_length=10)
    def __str__(self):
        return self.title

class Electrocardiographic(models.Model):
    # normal, abnormality , hyperthrophy
    title = models.CharField(max_length=10)
    def __str__(self):
        return self.title

class Angina(models.Model):
    # yes or no
    title = models.CharField(max_length=10)
    def __str__(self):
        return self.title

class St_segment(models.Model):
    # upsloping, flat, downsloping
    title = models.CharField(max_length=10)
    def __str__(self):
        return self.title

class ThalliumResult(models.Model):
    # Good, bad
    title = models.CharField(max_length=10)
    def __str__(self):
        return self.title

class Paitent(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(max_length=3)
    sex = models.ForeignKey(Sex, on_delete=CASCADE)
    chest_pain = models.ForeignKey(ChestPain, on_delete=CASCADE)
    blood_pressure = models.IntegerField(max_length=3)
    cholestorol = models.IntegerField(max_length=3)
    blood_sugar = models.IntegerField(max_length=3)
    electrocardiographic_resulter = models.ForeignKey(Electrocardiographic, on_delete=CASCADE)
    heart_rate = models.IntegerField(max_length=3)
    angina = models.ForeignKey(Angina, on_delete=CASCADE)
    st_depression = models.FloatField(max_length=5)
    st_segment = models.ForeignKey(St_segment, on_delete=CASCADE)
    vessels = models.IntegerField(max_length=2)
    thallium_test_result = models.ForeignKey(ThalliumResult, on_delete=CASCADE)


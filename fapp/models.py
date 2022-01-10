from django.db import models
from django.db.models import fields
from rest_framework import serializers
# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    time1 = models.TimeField(auto_now=True)

    def __str__(self):
        return self.title

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'
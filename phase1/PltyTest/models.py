from django.db import models
from django import forms
from django.forms.fields import ChoiceField
from django.forms.widgets import RadioSelect

class Poll(models.Model):
        question = models.CharField(max_length=200)
        votes= models.IntegerField()
        
        def __unicode__(self):
                return self.question


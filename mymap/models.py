from django.db import models
from datetime import datetime

class complaint(models.Model):
	ID=models.AutoField(primary_key=True)
	Location=models.CharField(max_length=100)
	Type=models.CharField(max_length=50)
	Category=models.CharField(max_length=100)
	Message=models.CharField(max_length=300,null=True,blank=True)
	Time=models.DateTimeField(default=datetime.now(),null=True,blank=True)
	Published=models.BooleanField(default=True)

	def __unicode__(self):
		ID=str(self.ID)
        	return ID

# Create your models here.

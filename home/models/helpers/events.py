from django.db import models

class EventVisitor(models.Model):
  
    first_name = models.CharField(max_length=40, null=False)
    last_name = models.CharField(max_length=40, null=False)
    company = models.CharField(max_length=30, null=False)
    brings_guest = models.BooleanField(default=False)
    email = models.EmailField(max_length=90, null=False)

    class Meta:
		    verbose_name = 'visitor'
		    verbose_name_plural = 'visitors'
		    ordering = ['last_name', 'first_name']


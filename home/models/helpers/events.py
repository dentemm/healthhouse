from django.db import models

from ..snippets import Event

class EventVisitor(models.Model):
  
    first_name = models.CharField('First name', max_length=40, null=False)
    last_name = models.CharField('Last name', max_length=40, null=False)
    company = models.CharField('Company / Organisation', max_length=30, null=False)
    email = models.EmailField('Email', max_length=90, null=False)
    phone = models.CharField('Phone number', max_length=16, blank=True, null=True)
    event = models.ForeignKey(Event, related_name='visitors', on_delete=models.CASCADE, null=True, blank=True)
    diet_info = models.TextField('Diet info', null=True, blank=True)

    def __str__(self):
        return self.last_name + ' ' + self.first_name

    class Meta:
		    verbose_name = 'visitor'
		    verbose_name_plural = 'visitors'
		    ordering = ['last_name', 'first_name']


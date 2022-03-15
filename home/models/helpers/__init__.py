from django.db import models

from wagtail.core.models import Orderable
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, FieldRowPanel

from django_countries.fields import CountryField

class TimeStampMixin(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True

class Address(models.Model):

	city = models.CharField(max_length=40)
	postal_code = models.CharField(max_length=8)
	street = models.CharField(max_length=40)
	number = models.CharField(max_length=8)
	country = CountryField(null=True, default='BE')

	class Meta:
		verbose_name = 'address'
		verbose_name_plural = 'addresses'
		ordering = ['city', ]
			
	def __str__(self):
		return '%s - %s' % (self.city, self.street)

Address.panels = [
	MultiFieldPanel([
		FieldRowPanel([
			FieldPanel('street', classname='col8'),
			FieldPanel('number', classname='col4')
		]
	),
	FieldRowPanel([
		FieldPanel('city', classname='col8'),
		FieldPanel('postal_code', classname='col4')
	]),
	FieldRowPanel([
		FieldPanel('country', classname='col6'),
		]),
	],
	heading='Address details'
	)
]

class GeneralBullet(Orderable, models.Model):

	item = models.CharField(max_length=128)

	def __str__(self):
		return self.item

	class Meta:
		ordering = ['sort_order']

GeneralBullet.panels = [
	FieldPanel('item')
]
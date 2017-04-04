from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

import datetime
from django.utils import timezone


# Create your models here.



@python_2_unicode_compatible
class Item(models.Model):
	code = models.CharField(max_length=20, primary_key=True)
	label = models.CharField(max_length=200)
	unit = models.CharField(max_length=100)
	# characteristics = models.ManyToManyField(Characteristic, related_name="characteristics")

	def __str__(self):
		return str(self.label) + "-" + str(self.code)

@python_2_unicode_compatible
class Characteristic(models.Model):
	name = models.CharField(max_length=200)
	enName = models.CharField(max_length=200)
	char_type = models.IntegerField() # this field is called type in the xml
	isProperty = models.BooleanField()
	specify = models.BooleanField()
	item = models.ForeignKey(Item)

	def __str__(self):
		return str(self.name)


@python_2_unicode_compatible
class Observation(models.Model):
	obeservation_number = models.IntegerField(blank=True)
	obs_time = models.DateField()
	shop_type = models.IntegerField()
	shop_identifier = models.CharField(max_length=200)
	flag = models.CharField(max_length=4)
	discount = models.CharField(max_length=4)
	value = models.DecimalField(decimal_places=4, max_digits=25)
	brand = models.CharField(max_length=200, blank=True)
	observed_quantity = models.DecimalField(decimal_places=4, max_digits=25)
	item = models.ForeignKey(Item)
	observer = models.ForeignKey(User, blank=True, related_name='observer', null=True)
	obs_comment = models.CharField(max_length=300, blank=True)
	

	def __str__(self):
		return str(self.item) + " " + str(self.obs_time)

@python_2_unicode_compatible
class UserObservation(models.Model):
	observation = models.ForeignKey(Observation)
	user = models.ForeignKey(User)

	def __str__(self):
		return str(self.user)

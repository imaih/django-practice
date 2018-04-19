from django.db import models



# Create your models here.

class Signup(models.Model):
	name = models.CharField(max_length=20)
	phone = models.IntegerField()
	email = models.EmailField()

	def __str__(self):
		return self.name

from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers
# Create your models here.

categories = (
	("Transfer News", "Transfer News"),
	("Press Release", "Press Release"),
	("Basket Ball", "Basket Ball"),
	("Table Tennis", "Table Tennis"),
	("Scrabble", "Scrabble"),
	("Chess", "Chess"),
	("Handball", "Handball"),
	("Soccer", "Soccer"),
	("Volley Ball", "Volley Ball"),
	("Chess", "Chess"),
	("Atlethics", "Athletics"),
	)

class Post(models.Model):
	identity = models.AutoField(primary_key = True)
	title = models.CharField(max_length=500, null=False)
	content = models.CharField(max_length = 10000000000000000000, null=False)
	author = models.ForeignKey(User)
	category = models.CharField(max_length = 200, choices=categories)
	pub_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "{}".format(self.title)


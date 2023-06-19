from django.db import models
class simsdata(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=100)

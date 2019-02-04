from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=40)


class Payment(models.Model):
    user = models.ForeignKey(User)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_id = models.CharField(max_length=40,db_index=True,null=True)
    status = models.NullBooleanField()
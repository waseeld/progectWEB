from django.db import models

# Create your models here.

class order(models.Model):
    first_name= models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    phone_number= models.CharField(max_length=40)
    id_order= models.CharField(max_length=30)


    def __str__(self):
       return self.first_name


class ConfirmOrder(models.Model):
    first_name1= models.CharField(max_length=50)
    last_name1= models.CharField(max_length=50)
    phone_number1= models.CharField(max_length=40)
    id_order1= models.CharField(max_length=30)
    order_number1= models.CharField(max_length=30)


    def __str__(self):
        return self.first_name1
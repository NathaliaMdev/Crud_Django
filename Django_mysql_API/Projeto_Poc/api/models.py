from django.db import models

# Create your models here.

  
#class Customer(models.Model):
   # id = models.IntegerField(primary_key=True)
    #name= models.CharField(max_length=40)
   # created_at=models.DateTimeField()
   # updated_at=models.DateTimeField()

   # class Meta:
   #   db_table = "customer"


class ProducerItem(models.Model):
    id = models.IntegerField(primary_key=True)
    name= models.CharField(max_length=40)
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()
    value = models.FloatField()
   # customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)

    class Meta:
      db_table = "produceritems"

  


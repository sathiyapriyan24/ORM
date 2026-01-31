from django.db import models
from django.contrib import admin
class swiggyDB(models.Model):
	oderID=models.IntegerField(primary_key=True)
	foodName=models.CharField(max_length=10)
	foodamount=models.FloatField()
	Email=models.EmailField()
	orderdate=models.DateField()
	Mobile_no=models.IntegerField()
	address=models.CharField(max_length=30)
	deliveryamount=models.FloatField()
class swiggyDBAdmin(admin.ModelAdmin):
	list_display=['oderID','foodName','foodamount','Email','orderdate','Mobile_no','address','deliveryamount'];

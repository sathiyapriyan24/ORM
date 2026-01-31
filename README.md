# Ex02 Django ORM Web Application
## Date: 30.01.2026

## AIM
To develop a Django Application to store and retrieve data from a E-Commerce Website Database for Amazon or Flipkart using Object Relational Mapping(ORM).


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
~~~
models.py

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

admin.py

from django.contrib import admin
from .models import swiggyDB,swiggyDBAdmin 
admin.site.register(swiggyDB,swiggyDBAdmin)

~~~


## OUTPUT
![alt text](<Screenshot 2026-01-30 144415.png>)



## RESULT
Thus the program for creating E-commerce website database using ORM hass been executed successfully

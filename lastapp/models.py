from django.db import models
import MySQLdb
db=MySQLdb.connect('localhost','root','','lastproject')
cursor=db.cursor()

print('connection done....')


# Create your models here.


class Destination(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    password=models.CharField(max_length=200)

class rentee(models.Model):
    catid = models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=50)
    mobile_number=models.CharField(max_length=50)
    occupation=models.CharField(max_length=50)
    maritial_status=models.CharField(max_length=50)
    family_member=models.CharField(max_length=50)
     
class renter(models.Model):
        catid = models.AutoField(primary_key=True)
        name=models.CharField(max_length=50)
        email=models.CharField(max_length=30)
        phone_number=models.CharField(max_length=15)
        mobile_number=models.CharField(max_length=10)
        state=models.CharField(max_length=20)
        city=models.CharField(max_length=15)
        locality=models.CharField(max_length=20)
        house_number=models.CharField(max_length=10)
        landmark=models.CharField(max_length=20)
        no_of_rooms=models.CharField(max_length=5)
        kitchen=models.CharField(max_length=5)
        bathroom=models.CharField(max_length=5)
        #pica=models.ImageField(upload_to='media/pica',default='')
        #picb=models.ImageField(upload_to='media/picb',default='')
        #picc=models.ImageField(upload_to='media/picc',default='')
        location=models.CharField(max_length=20)
        message=models.CharField(max_length=50)
        electricity_charge=models.CharField(max_length=50)
        water_charge=models.CharField(max_length=50)
        rent_value=models.CharField(max_length=50)
"""
class renterimage(models.Model):
        pic1=models.ImageField(upload_to='media/pic1',default='')
        pic2=models.ImageField(upload_to='media/pic2',default='')
        pic3=models.ImageField(upload_to='media/pic3',default='')

        """

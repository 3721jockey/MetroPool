from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Registration(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    add=models.CharField(max_length=100)
    con=models.BigIntegerField()
    psw=models.CharField(max_length=20)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

class StopsM(models.Model):
    stopname=models.CharField(max_length=50)

class StopsW(models.Model):
    stopname=models.CharField(max_length=50)

class MetroBook(models.Model):
    start=models.CharField(max_length=30)
    stop=models.CharField(max_length=30)
    amount=models.CharField(max_length=30)
    status=models.CharField(max_length=30)
    srStatus=models.CharField(max_length=30,default="Not Booked")
    time=models.TimeField(null=True)
    qr=models.CharField(max_length=100,null=True)
    user = models.ForeignKey(Registration,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)

class WaterBook(models.Model):
    start=models.CharField(max_length=30)
    stop=models.CharField(max_length=30)
    amount=models.CharField(max_length=30)
    status=models.CharField(max_length=30)
    time=models.TimeField(null=True)

    qr=models.CharField(max_length=100,null=True)
    user = models.ForeignKey(Registration,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    

class Payment(models.Model):
    mBid=models.ForeignKey(MetroBook,on_delete=models.CASCADE,null=True)
    wBid=models.ForeignKey(WaterBook,on_delete=models.CASCADE,null=True)
    uid=models.ForeignKey(Registration,on_delete=models.CASCADE,null=True)
    date=models.DateField(auto_now_add=True)
    amt=models.FloatField()


class FoodRequest(models.Model):
    request=models.CharField(max_length=100)
    stop = models.CharField(max_length=30)

class Schedule(models.Model):
    mName = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    

    

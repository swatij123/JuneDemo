from django.db import models
from django.contrib.auth.models import User
import django_tables2 as tables
from phonenumber_field.modelfields import PhoneNumberField


class Client(models.Model):
    
    ClientName= models.CharField(max_length=200,blank=False,unique=True,error_messages ={
                    "unique":"Client Already exist."
                    })
    Currency = models.CharField(max_length=100, blank=False)
    BillingMethod = models.CharField(max_length=100, blank=False)
    
    def __str__(self):
        return self.ClientName
    

class ClientContact(models.Model):
  
  ClientName = models.ForeignKey(Client, on_delete=models.CASCADE)
  Emailid = models.EmailField(max_length=200, blank=False)
  FirstName = models.CharField(max_length=200, blank=False)
  LastName = models.CharField(max_length=200, blank=True)
  Phone = PhoneNumberField(null=False, blank=False)
  Mobile = PhoneNumberField(null=False, blank=True)
  Fax = models.CharField(max_length=200, blank=True)

  def __str__(self):
        return self.ClientName
  
        
# Create your models here.

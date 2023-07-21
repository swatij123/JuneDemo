from msilib.schema import tables
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from numpy import require
from .models import Client, ClientContact

Currency_Choice =[('AUD','AUD'),
                  ('EUR','EUR'),
                 ('INR','INR'),           
                 ('JPY', 'JPY'),
                 ('USD','USD'),
            
]

Billing_Choice =[('Hourly Job Rate','Hourly Job Rate'),
('Hourly User Rate','Hourly User Rate'),
('Hourly User Rate - Jobs','Hourly User Rate - Jobs'),
('Hourly User Rate - Projects','Hourly User Rate - Projects'),

]
class clientContact(forms.ModelForm):
    
    Emailid=forms.EmailField(label='Email Id')
    FirstName=forms.CharField(label='First Name')
    LastName=forms.CharField(label='Last Name')
    
    class Meta:
        model = ClientContact
        fields = ['ClientName','Emailid','FirstName','LastName','Phone','Mobile','Fax']
        
        

class client(forms.ModelForm):
    ClientName= forms.CharField(label='Client Name',max_length=30)
    Currency= forms.CharField(label='Currency',widget=forms.Select(choices=Currency_Choice))
    BillingMethod= forms.CharField(label='Billing Method',widget=forms.Select(choices=Billing_Choice))
    class Meta:
        model =Client
        fields = ['ClientName','Currency','BillingMethod']



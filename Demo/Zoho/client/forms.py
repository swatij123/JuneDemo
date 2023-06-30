from msilib.schema import tables
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Client, ClientContact

Currency_Choice =[('INR','INR'),
           ('USD','USD'),
           ('EUR','EUR'),
            ('JPY', 'JPY'),
            ('AUD','AUD'),
]

Billing_Choice =[('Hourly Job Rate','Hourly Job Rate'),
('Hourly User Rate','Hourly User Rate'),
('Hourly User Rate - Jobs','Hourly User Rate - Jobs'),
('Hourly User Rate - Projects','Hourly User Rate - Projects'),

]
class clientContact(forms.ModelForm):
    class Meta:
        model = ClientContact
        fields = ['ClientName','Emailid','FirstName','LastName','Phone','Mobile','Fax']
        

class client(forms.ModelForm):
    ClientName= forms.CharField(max_length=30)
    Currency= forms.CharField(label='Currency',widget=forms.Select(choices=Currency_Choice))
    BillingMethod= forms.CharField(label='Currency',widget=forms.Select(choices=Billing_Choice))
    class Meta:
        model =Client
        fields = ['ClientName','Currency','BillingMethod']



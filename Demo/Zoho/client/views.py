from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Client, ClientContact
from django.template import loader
from .forms import client
from .forms import clientContact
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    mymembers = Client.objects.all().order_by('ClientName').values()
    template = loader.get_template('client/home.html')
    context = {
    'mymembers': mymembers,
  }
    return HttpResponse(template.render(context, request))
@login_required
def AddClient(request):
   
    if request.method == "POST":
        form = client(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/profile')
    else:
          form = client()
    return render(request, 'client/register.html', {'form': form})
   
    
def ClientProfile(request):
    if request.method == "POST":
        form = clientContact(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = clientContact()
    return render(request, 'client/profile.html', {'form': form})

def view(request,id):
    clientname=Client.objects.filter(id=id).values()
    member= ClientContact.objects.filter(ClientName_id=id).values()
    print(member)
    print(clientname)
    template = loader.get_template('client/view.html')
    context = {
    'member':member,
    'clientname' :clientname,
  }
    return HttpResponse(template.render(context, request))

def update(request, id):
    clientname=Client.objects.filter(id=id).values()
    mymember = ClientContact.objects.filter(ClientName_id=id).values()
    print(mymember)
    print(clientname)
    template = loader.get_template('client/update.html')
    context = {
       'mymember': mymember,
       'clientname' :clientname,
  }
    
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  Emailid = request.POST['Emailid']
  FirstName= request.POST['FirstName']
  LastName = request.POST['LastName']
  Phone= request.POST['Phone']
  MobileNumber = request.POST['MobileNumber']
  Fax =request.POST['Fax']
  
  member = ClientContact.objects.get(id=id)
  member.Emailid = Emailid
  member.FirstName= FirstName
  member.LastName= LastName
  member.Phone = Phone
  member.Mobile= MobileNumber
  member.Fax= Fax
  member.save()
  return HttpResponseRedirect(reverse('home'))

def delete(request, id):
    member = Client.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('home'))
# Create your views here.

from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from .models import Contact
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    if request.user.is_anonymous:
        return redirect('/accounts/login')
    return render(request, 'index.html')

def create(request):
    if request.method == "POST":
        phone_number = request.POST.get('phone')
        contacts = Contact.objects.filter(phone = phone_number)
        if len(contacts):
            contactExists = True
            return render(request, 'pages/create.html', {'formFilled' : True, 'contactExists': contactExists})
        contactExists = False
        selects = False
        first_name = request.POST.get('fname')                              # Get the input data from the users
        last_name = request.POST.get('lname')
        e_mail = request.POST.get('email')
        contact_address = request.POST.get('address')
        contact = Contact(selects=False, fname=first_name, lname=last_name, email=e_mail, phone = phone_number, address=contact_address, date=datetime.today(), createdBy = request.user.get_username())  #create an object of the class Contac
        contact.save()                                                       # and save it            
        formFilled = True
        return render(request, 'pages/create.html', {'formFilled' : formFilled , 'contactExists': contactExists})
    if request.user.is_anonymous:
        formFilled = False
        return redirect('/accounts/login')
    formFilled = False
    return  render(request, 'pages/create.html')

def remove(request):
    if request.user.is_anonymous:
        return redirect('/accounts/login')
    if request.method == "POST":
        contacts = Contact.objects.filter(createdBy = request.user.get_username()).order_by('fname')
        print("list : ", contacts)
        for contact in contacts:
            print(request.POST.get('select'))
            if request.POST.get('select') == True: 
                contact.delete()
        return render(request, 'pages/remove.html')
    else:
        try:
            contacts = Contact.objects.filter(createdBy = request.user.get_username()).order_by()
            empty = False
            if not len(contacts):
                empty = True
            return render(request, 'pages/remove.html', {'contacts': contacts, 'empty': empty})
        except:
            contacts = Contact.objects.filter(createdBy = request.user.get_username())
            return render(request, 'pages/remove.html', {'contacts': contacts, 'empty': True})


def req(request):                                                           # to request for a change
    if request.user.is_anonymous:
        return redirect('/accounts/login')
    return render(request, 'pages/request.html')    

def database(request):                                                      # to show all the userdata
    searchComplete = False
    if request.user.is_anonymous:
        return redirect('/accounts/login')
    if request.method == "POST":
        search = request.POST.get('search') 
        try:
            contacts = Contact.objects.order_by('fname')
            listOfContacts = list()
            for contact in contacts:
                foundFlag = 0
                attr = [contact.fname, contact.lname, contact.email, contact.createdBy]
                attrNumeric = [contact.email, contact.phone]
                if search.isnumeric():
                    if not foundFlag:
                        for info in attrNumeric:
                            if search.strip().lower() in info.strip().lower():
                                print("FOUMNDDD: ", search, info, type(info))
                                searchComplete = True
                                listOfContacts.append(contact)
                                foundFlag = 1
                                break
                            else:
                                print("NOT FOUND: ", search, info, type(info))
                                print("NOT FOUND: ", search, contact.fname)
                else:
                    if not foundFlag:
                        for info in attr:
                            if search.strip().lower() in info.strip().lower():
                                print("FOUMNDDD: ", search, info, type(info))
                                searchComplete = True
                                listOfContacts.append(contact)
                                foundFlag = 1
                                break
                            else:
                                print("NOT FOUND: ", search, info, type(info))
                                print("NOT FOUND: ", search, contact.fname)
            return  render(request, 'pages/database.html', {'searchComplete' : searchComplete, 'contacts' : listOfContacts})
        except:
            return render(request, 'pages/database.html', {'searchComplete' : False})
    return render(request, 'pages/database.html')
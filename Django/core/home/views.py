from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    people = [
        {'name': 'Abdul Qadeer', 'age': 26},
        {'name': 'Tanveer Khalil', 'age': 20},
        {'name': 'Alishba Khalil', 'age': 16},
        {'name': 'Aneela Khalil', 'age': 14},
        {'name': 'Alisha Khalil', 'age': 12}]
    return render(request, "index.html", context={'peoples': people, 'page': 'Home'})


def contact_us(request):
    context = {'page': 'Contact Us'}
    return render(request, "contact.html", context)


def about_us(request):
    context = {'page': 'About Us'}
    return render(request, "about.html", context)

from django.http import HttpResponse
from django.shortcuts import render
def homePage(request):
    data={
        'title':"Home Page",
        'bdata':"Welcome to Django App",
        'courseList':["Python","Java","PHP","Java Script"],
        'numbers':[10,20,30,40,50],
        'studentDetails':[
            {'name':"AQ",'phone':"03154366906"},
            {'name':"Khawaja",'phone':"03003796906"}
        ]

    }
    return render(request,"index.html",data)


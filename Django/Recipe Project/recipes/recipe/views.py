
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *

# Create your views here.


def recipes(request):
    if request.method == "POST":
        data = request.POST
        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")
        recipe_image = request.FILES.get("recipe_image")
    

   
        ReciepesAdd.objects.create(
            recipe_name = recipe_name,
            recipe_description = recipe_description,
            recipe_image = recipe_image,

        )
        latest_recipe = ReciepesAdd.objects.latest('id')
        return redirect(f'/?latest_recipe={latest_recipe.id}')
    qureyset = ReciepesAdd.objects.all()
    context = {'page':"Recipe",'recipe':qureyset}

    # return HttpResponse("Welcome Reciepes Page")
    return render(request, "recipe.html",context)

def home(request):
    
   
    context = {'page':"Home"}
    return render(request, "index.html",context)
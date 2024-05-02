from django.shortcuts import render
from .forms import BoxeurForm
from . import models

# Create your views here.
def index(request):
    return render(request, 'myfirstpalmaresapp/index.html')

def ajout(request):
    if request.method == "POST":
        form = BoxeurForm(request)
        if form.is_valid(): # validation du formulaire.
            Livre = form.save() # sauvegarde dans la base
            return render(request,"myfirstpalmaresapp/affiche.html",{"Livre" : Livre})
        else:
            return render(request,"myfirstpalmaresapp/ajout.html",{"form": form})
    else:
        form = BoxeurForm() # création d'un formulaire vide
        return render(request,"myfirstpalmaresapp/ajout.html",{"form" : form})

def traitement(request):
    lform = BoxeurForm(request.POST)
    if lform.is_valid():
        Boxeur = lform.save()
        return render(request,"myfirstpalmaresapp/affiche.html",{"Boxeur" : Boxeur})
    else:
     return render(request,"myfirstpalmaresapp/ajout.html",{"form": lform})
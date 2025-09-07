from django.shortcuts import render

def renderTemplate(request):
    return render(request,'Registro.html')
from contextvars import Context
from datetime import datetime
from pipes import Template
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.template import Template, Context
from django.template import loader
from App_Coder.models import Familiares, Datos

def familiares(self):
    familiar = Familiares (nombre = "Daniel", apellido = "Pacheco", ult_edic = datetime.fromisoformat('2011-11-04'))
    familiar.save()
    
    documentoDeTexto = f"--->Nombre: {familiar.nombre} Apellido: {familiar.apellido} Ultima Edición: {familiar.ult_edic}"

    obj = Familiares.objects.all()

    return render (self, "Familiares.html", {"obj": obj[0]})

def datosDeFamiliares (self):
    dato = Datos (telefono = "5581528503", edad = "21")
    dato.save()

    documentoDeTexto = f"--->Numero de Telefono: {dato.telefono} Edad: {dato.edad}"

    obj = Familiares.objects.all()

    return render (self, "Datos.html", {"obj": obj})  


#def template1 (self):

    nombre = "Daniel" 
    apellido = "Pacheco"

    diccionario = {"nombre": nombre, "apellido": apellido}

    plantilla = loader.get_template("Template.html")

    documento = plantilla.render (diccionario)

    return HttpResponse(documento)
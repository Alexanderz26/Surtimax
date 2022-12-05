from django.shortcuts import render
from django.http import HttpResponse
from compras.models import Compra 

# Create your views here.
def compras(request):
    return render (request, 'compras/compras.html')

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def holamundo(request):
    return HttpResponse('Productos')

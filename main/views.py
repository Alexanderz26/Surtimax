from django.shortcuts import render

def inicioAdmin(request):
   
    context = {     
    }
    return render(request,'index.html',context)




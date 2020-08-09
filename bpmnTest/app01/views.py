from django.shortcuts import render

# Create your views here.
def models(request):
    return render(request,"models.html")

def viewer(request):
    return render(request,"viewer.html")
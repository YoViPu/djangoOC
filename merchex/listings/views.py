from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band


def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', {'bands': bands})

def about(request):
    return HttpResponse("<h1>About us : Nous somme Yoann</h1>")

def listings(request):
    return HttpResponse("<h1>Listings</h1>")

def contact(request):
    return HttpResponse("<h1>Contact</h1> <p>Contact us at 07 70 38 09 40</p>")

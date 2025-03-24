from django.shortcuts import render
from django.http import HttpResponse

def pagrindinis(request):
    kontekstas = {
        'pavadinimas': 'Mano Puslapis',
        'antraste': 'Welcome to my main page'
    }
    return render(request, 'pagrindinis.html', kontekstas)

def apie(request):
    context = {
        'pavadinimas': 'Apie mus',
        'antraste': 'Apacioje rasite texta'
    }
    return render(request, 'apie.html', context)

def kontaktai(request):
    return HttpResponse('You can contact us on this dead url i havent even posted')

def naujienos(request):
    content = {
        'pavadinimas': 'Naujienos',
        'antraste': 'Svieziausios naujienos!'
    }
    return render(request, 'naujienos.html', content)

def author(request):
    context = {
        'vardas': 'Jonas',
        'pomegiai': [
            'Coding', 'Coffee', 'randomly changing language mid task', 'bikes'
        ]
    }
    return render(request, 'author.html', context)
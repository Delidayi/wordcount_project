from django.http import HttpResponse
from django.shortcuts import render
import operator

# hieronder wordt gerefereed naar startpagina van website dus wordcout.com
def homepage(request):
    return render(request, 'home.html') # zie templetes home.html

# hierwordt je geleid naar wordcount.com/tellen
def tellen(request):
    volledigtext = request.GET['volledigtext'] # de tekst die de user ingeeft wordt opgelagen in variable

    woordenlijst = volledigtext.split() # nieuwe variable wordt gecreerd met gespitste woorden er in met spaties

    woorden_na_telling = {} # een lege dictonory lijst wat wordt gevuld met onderstaande for loop

    for woorden in woordenlijst: # alle woorden in de woordenlijst worden nagelopen per woord wordt er geteld
        if woorden in woorden_na_telling:
            # verhoog de aantal
            woorden_na_telling[woorden] += 1 # als woord bekent dan wordt er 1 bijgeteld
        else:
            # toevoegen aan de woordenlijst
            woorden_na_telling[woorden] = 1 # wanneer woord is nieuw wordt het toegevoegd in lijst

        gesorteerde_woorden = sorted(woorden_na_telling.items(), key=operator.itemgetter(1), reverse=True) # hier worden de getelde woorden gesorteerd

    return render(request, 'tellen.html', {'volledigtext':volledigtext, 'aantal_woorden':len(woordenlijst),
    'gesorteerde_woorden':gesorteerde_woorden})

def overons(request):
    return render(request, 'about.html')

from django.http import HttpResponse
#ab mai templates ko use karne ke liya import marronga tut 8
from django.shortcuts import render

def about(request):
    return render(request, 'about us.html')

def contact(request):
    return render(request, 'contact us.html')

def index(request):
    return render(request,'index.html')



def analyze(request):
    # Get the text
    djtext = request.POST.get('text','default')
    # jo mera djtext thaa wo text thaa jo mera text input kiya gya website per wo djtext roop maine le liya ek barr mera pass djtext aagyq

    # Check checkbox values
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    #Quick Quiz
    charactercount = request.POST.get('charcount', 'off')

    # Check which checkbox is on
    # maine kahaa agar
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
       # jo mera djtext variable hai wo mine overide kiya

# or maine kaha phirse check kro
    if(fullcaps == "on"): #check kiya
        analyzed = ""
        for char in djtext: #wotext hia jo kee input kiy hai
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if(newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            # esk ye problem hai kee new line charcter ke sath sath ek charje retun bhee check karne padega jo newline hoota hai
            # ye network mai new line charcter ko transport karne ke liya el \n or \r dono dalajte hia
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

#Agr do character eksaath mujhe milgya jo ke space hai onmai se ek choup hoojye
    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed


    #Quick Quix
    # Character Count
    if(charactercount == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = len(djtext)
        params = {'purpose': 'Character Counting', 'input': djtext, 'analyzed_text': analyzed}

    if (removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on" and charactercount != "on"):
        return HttpResponse("Please select any operation  and try again")
    return render(request, 'analyze.html', params)


# AJW
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return (
        render(request, 'index.html')
    )

def contact(request):
    return (
        render(request, 'contact.html')
    )

def about(request):
    return (
        render(request, 'about.html')
    )

def analyze(request):

    # Get the text from textarea
    djtext = request.POST.get("text", "default")

    # Get the checkboxes
    removepunc = request.POST.get("removepunc", "off")
    uppercase = request.POST.get("uppercase", "off")
    lowercase = request.POST.get("lowercase", "off")
    newlineremove = request.POST.get("newlineremover", "off")
    extraspaceremove = request.POST.get("extraspaceremover", "off")
    charcount = request.POST.get("charcount", "off")

    # Remove Puntuation 
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {"purpose":"Removed Puntuations", "analyzed_text": analyzed}
        djtext = analyzed

    # Uppercase 
    if uppercase == "on":
        analyzed = djtext.upper()
        params = {"purpose":"Uppercased", "analyzed_text": analyzed}
        djtext = analyzed

    # Lowercase
    if lowercase == "on":
        analyzed = djtext.lower()
        params = {"purpose": "Lowercased", "analyzed_text": analyzed}
        djtext = analyzed

    # Remove New Line
    if newlineremove == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {"purpose": "Newline Removed", "analyzed_text": analyzed}
        djtext = analyzed
        
    # Remove Extra Space 
    if extraspaceremove == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {"purpose": "Extra Sapced Removed", "analyzed_text": analyzed}
        djtext = analyzed

    # Count the total characters 
    if charcount == "on":
        count = 0
        for char in djtext:
            count += 1
        analyzed = count
        params = {"purpose": "Total Character Counted", "analyzed_text": analyzed}

    if removepunc != "on" and uppercase != "on" and lowercase != "on" and newlineremove != "on" and extraspaceremove != "on" and charcount != "on":
        return (render(request, 'error.html'))

    return (render(request, "analyze.html", params))


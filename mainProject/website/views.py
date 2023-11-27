from django.shortcuts import render
from django.http import HttpResponse

def hello_test(request):
    gamesList = ['Bioshock Infinite', 'The Great Ace Attorney Chronicles', 'Barony', 'Slay The Spire', 'Dont Starve Together']
    data = {'name': 'Deusana', 'gamesList': gamesList}
    return render(request, 'index.html', data)
    # return HttpResponse("Welcome to the website!")
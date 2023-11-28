from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def hello_test(request):
    gamesList = ['Bioshock Infinite', 'The Great Ace Attorney Chronicles', 'Barony', 'Slay The Spire', 'Dont Starve Together']
    postList = Post.objects.all()
    data = {
        'name': 'Deusana',
        'gamesList': gamesList,
        'postList': postList
        }    

    return render(request, 'index.html', data)
    # return HttpResponse("Welcome to the website!")

def post_detail(request, id):
    post = Post.objects.get(id = id)
    post_detail = {'post': post}

    return render(request, 'post_detail.html', post_detail)
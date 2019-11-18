from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.shortcuts import render_to_response
from main.models import *
# Create your views here.

def main(request):
    return render(request, 'main/main.html', locals())

def news(request):
    newses = News.objects.all()
    return render(request, 'news/news.html', locals())

def faq(request):
    return render(request, 'faq/faq.html', locals())

def contacts(request):
    context = {

    }
    return render(request, 'contacts/contacts.html', locals())


def game(request):
    return render(request, 'game/src/game.html', locals())

from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories
def index(request):
    categories = Categories.objects.all()
    context = {
        'title' : 'Home - Главная',
        'content' : "Магазин мебели Home",
        'categories' : categories,
     }
    return render(request, 'main/index.html',context)
def about(request):
    context = {
        'title' : 'About',
        'content' : 'About us',
        'text_on_page' : 'Here text about us'
    }
    return render(request, 'main/about.html',context)


from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.http import Http404
from myapp.models import Menu


# Create your views here.
# 메인 페이지
def app_main(request):
    today = datetime.today().date()
    context = {"date": today}
    return render(request, 'menus/index.html', context=context)


# 메뉴 페이지
def app_menu(request):
    today = datetime.today().date()
    menus = Menu.objects.all()
    eng=[]
    for i in menus:
        eng.append(i.img_path.split('/')[-1].replace('.jpg',''))
    context = {
        "date": today,
        'Menus': menus,
        'eng': eng,
    }
    return render(request, 'foods/index.html', context=context)


# 디테일 페이지
def food_detail(request, food):
    foods = Menu.objects.get(img_path__contains=food)
    if foods:
        context = {"food": foods}
    else:
        raise Http404
    return render(request, 'foods/detail.html', context=context)

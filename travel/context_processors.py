
from django.shortcuts import render
from travel. models import Category, SubCategory, AllCategory



def category(request):
    cat1 = Category.objects.all()
    return {"cat1": cat1}


def subcategory(request):
    cat2 = SubCategory.objects.all()
    return {"cat2": cat2}


def allcategory(request):
    cat3 = AllCategory.objects.all()
    return {"cat3": cat3}
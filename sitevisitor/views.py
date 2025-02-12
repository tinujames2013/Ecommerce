from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
    products = Product.objects.all()
    context ={
        'products': products
    }
    return render(request,'sitevisitor/home.html',context)
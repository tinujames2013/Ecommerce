from django.shortcuts import render, get_object_or_404, redirect
from sitevisitor.models import Product,Category

# Create your views here.
def home(request):
    products = Product.objects.all()
    context ={
        'products': products
    }
    return render(request,'adminpanel/home.html',context)

def add_product(request):
    categories = Category.objects.all()
    if request.method =='POST':
        name = request.POST.get('product_name')
        description = request.POST.get('product_description')
        image = request.FILES.get('product_image')
        price = request.POST.get('product_price')
        stock = request.POST.get('product_stock')
        category_id = request.POST.get('product_category')
        category = get_object_or_404(Category, id = category_id)
        Product.objects.create(
            name = name,
            description = description,
            product_photo = image,
            price = price,
            stock = stock,
            category = category 
        )
    context ={
            'categories':categories
        }

    return render(request,'adminpanel/add_product.html',context)

def edit_product(request, product_id):
    product = get_object_or_404(Product,id = product_id)
    categories = Category.objects.all()
    if request.method =='POST':
        product.name = request.POST.get('product_name')
        product.description = request.POST.get('product_description')    
        product.price = request.POST.get('product_price')
        product.stock = request.POST.get('product_stock')
        category_id = request.POST.get('product_category')
        product.category = get_object_or_404(Category, id = category_id)
        image = request.FILES.get('product_image')
        if image:
            product.product_photo = image
        product.save()
    context = {
        'categories': categories,
        'product':product
    }    

    return render(request,'adminpanel/edit_product.html',context)

def delete_product(request, product_id):
    product =get_object_or_404(Product,id = product_id)    
    product.delete()
    return redirect('adminpanel:home')


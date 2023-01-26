from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from cart.models import Product
from django.db.models import Q
from django.contrib import messages


# Create your views here.
@login_required
def view_product(request):
    page_number = request.GET.get('page_num', 1)
    if page_number is None:
        page_number = 1
    products = Product.objects.all().order_by('price')
    paginator = Paginator(products, 15)
    products_page = paginator.get_page(page_number)
    return render(request, "home.html", context={'products':products_page})

@login_required
def search_recommendation(request):
    if request.method == 'GET':
        location = request.GET.get("location", "")
        shape = request.GET.get("shape", "")
        price_range_min = request.GET.get("price_range_min", None)
        price_range_max = request.GET.get("price_range_max", None)
        page_num = request.GET.get('page_num', 1)
        products = products = Product.objects.filter(Q(location=location) | Q(price__range=(price_range_min, price_range_max)) | Q(shape=shape)).order_by('price')
        paginator = Paginator(products, 15)
        products_page = paginator.get_page(page_num)
        context = {
            'location':location,
            'shape':shape,
            'price_min':price_range_min,
            'price_max':price_range_max,
            'page_num':page_num,
            'products':products_page,
        }
        return render(request, "recoomendation.html", context=context)
    return render(request, "recoomendation.html")

def add_product(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        shape = request.POST.get('shape')
        size = request.POST.get('size')
        price = request.POST.get('price')

        Product.objects.create(shape=shape, location=location, size=size, price=price)
        messages.success(request, "Data Saved Successfully")
        return redirect('home')
    else:
        return redirect('home')
from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q

def main(request):

    a = Typeproduct.objects.all()
    context = {'content': [
        {'producttype':producttype, 'products': Product.objects.filter(typeproduct = producttype)} for producttype in a 
    ]}
    
    if request.method == 'POST':
        search = request.POST.get('search')
        products = Product.objects.filter(Q(title__icontains=search) |
        Q(description__icontains=search) | Q(mayker__icontains=search))
        context['products'] = products
    return render(request, 'products/main.html', context=context)

def productview(request, id):
    
    if request.method == 'POST':
        return main(request)
    else:
        product = Product.objects.get(pk = id)
        context = {'product': product}
        return render(request, 'products/product.html', context=context)



# Create your views here.

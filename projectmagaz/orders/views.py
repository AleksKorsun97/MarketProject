from django.shortcuts import render, redirect
from .models import *
from products.models import *

def backet(request):
    try :
        backet_user = Bucket.objects.get(user=request.user)
    except: 
        backet_user = Bucket.objects.create(user=request.user)
    context = {'products': backet_user.products.all()}
    return render(request,'orders/backet.html', context=context)

def add_product(request, id):
    try :
        backet_user = Bucket.objects.get(user=request.user)
    except: 
        backet_user = Bucket.objects.create(user=request.user)
    backet_user.products.add(Product.objects.get(pk=id))

    return redirect('main')

def delete_product(request, id):
    try :
        backet_user = Bucket.objects.get(user=request.user)
    except: 
        backet_user = Bucket.objects.create(user=request.user)
    backet_user.products.remove(Product.objects.get(pk=id))

    return redirect('backet')


def create_order_page(request):
    bucket = Bucket.objects.get(user = request.user)
    products = bucket.products.all()
    listprice = [product.price for product in products]
    context = {'products': products,'fullprice': sum(listprice)}
    if request.method == 'POST':
        post = request.POST.get('number_post')
        number = request.POST.get('number_phone')
        city = request.POST.get('city')
        surname = request.POST.get('surname')
        if post and number and city and surname:
             
            obj = Order.objects.create(user = request.user, status = 0, 
            name_surname = surname, city = city, post = post, number = number)
            for product in products:


                obj.products.add(product.id)
            obj.save()
            # for product in products:
            #     backet.products.remove(product)
    return render(request, 'orders/create.html', context=context)

def order_tracking(request, id):
    order = Order.objects.get(pk=id)
    products = order.products.all()

    listprice = [product.price for product in products]

    context={'products': products, 'order': order, 'fullprice': sum(listprice)}
    return render(request, "orders/order_tracking.html",context=context)


def orders_page(request):
    orders = Order.objects.filter(user = request.user)
    status_list = ['Чекає на оплату', "Готуєтся до відправлення", 
               "Відправлено", "На пошті", "Доставлено"]

    orders_list = [
        {'order':order, 
        'price': sum([product.price for product in order.products.all()]),
        'status': status_list[order.status]} 
        for order in orders]
    context = {'orders': orders_list}

    return render(request, "orders/orders_page.html", context=context)


# Create your views here.

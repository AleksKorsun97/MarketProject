from django.shortcuts import render
from django.views.generic import TemplateView
from products.models import *
from orders.models import *
from django.core.files.storage import FileSystemStorage

class KategoriView(TemplateView):
    def dispatch(self, request):
        context = {'Typeproduct': Typeproduct.objects.all()}
        self.create_kategori(request)

        
        return render(request, 'adminpanel/kategori.html', context=context)
    def create_kategori(self, request):
        if request.method == 'POST':
            title = request.POST.get('title')
            if title:
                Typeproduct.objects.create(title=title)




class ProductView(TemplateView):
    def dispatch(self, request):
        self.create_product(request)
        context = {'Product': Product.objects.all(), 
        'Typeproduct': Typeproduct.objects.all()}


        return render(request, 'adminpanel/products.html', context=context)
    
    def create_product(self, request):
        if request.method == 'POST':
            mayker = request.POST.get('mayker')
            material = request.POST.get('material')
            size = request.POST.get('size')
            title = request.POST.get('title')
            price = request.POST.get('price')
            image = request.FILES.get('image')
            description = request.POST.get('description')
            kategori = request.POST.get('kategori')
            if title and price and image and description and kategori and mayker and material and size:
                kategori = Typeproduct.objects.get(pk = kategori)
                fss = FileSystemStorage()
                file = fss.save(image.name, image)
                file_url = fss.url(file)
                Product.objects.create(title=title, price=price, description=description, image=file_url, typeproduct=kategori, material=material, size=size, mayker=mayker)





class OrderView(TemplateView):
    def dispatch(self, request, id = None):
        current_order = None
        products = None
        status_list = ['Чекає на оплату', "Готуєтся до відправлення", 
               "Відправлено", "На пошті", "Доставлено"]
        orders = Order.objects.all()

        if id != None:
            current_order = Order.objects.get(pk = id)
            products = current_order.products.all()
             
        if request.method == 'POST':
            status = request.POST.get('status')
            if status:
                current_order.status = status
                current_order.save()
        orders_list = [
            {'order':order, 'status':status_list[order.status]}
            for order in orders
        ]
        context = {'orders':orders_list, 'products':products, 'current_order':current_order}
        return render(request, 'adminpanel/order.html', context=context)



        
    
    

# Create your views here.

"""projectmagaz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from projectmagaz import settings
from django.conf.urls.static import static
from adminpanel.views import *
from products.views import *
from main.views import *
from orders.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kategori/',KategoriView.as_view()),
    path('product/', ProductView.as_view()),
    path('order/', OrderView.as_view()),
    path('order/<int:id>/', OrderView.as_view()),
    path('main/',main, name='main'),
    path('products/<int:id>/',productview),
    path('register/',register),
    path('autenfication/',auth, name='auth'),
    path('logout/',logoutuser),
    path('backet/',backet, name='backet'),
    path('addproduct/<int:id>/',add_product),
    path('delete/<int:id>/',delete_product),
    path('create/',create_order_page),
    path('tracking/<int:id>/',order_tracking),
    path('orderspage/',orders_page),
    


    
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

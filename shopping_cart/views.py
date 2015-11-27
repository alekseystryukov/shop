from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _


from forms import PurchaseForm
from models import *


def home(request):
    return render(request, 'shopping_cart/home.html',
                  {
                    'categories': Category.objects.annotate(product_count=Count('product'))
                  })


def products(request, category_id):
    cat = get_object_or_404(Category, pk=category_id)
    return render(request, 'shopping_cart/products.html',
                  {
                    'category': cat,
                    'products': Product.objects.filter(category=cat)
                  })


def product(request, product_id):
    prod = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            Purchase.objects.create(cart=Cart.get(request),
                                    product=prod,
                                    quantity=form.cleaned_data['quantity'])
            messages.success(request, _('Your purchase was successfully added to the Cart'))
    else:
        form = PurchaseForm(initial={'quantity': 1})
    return render(request, 'shopping_cart/product.html',
                  {
                    'product': prod,
                    'form': form
                  })


def cart(request):

    cart_obj = Cart.get(request)

    if request.POST.get('rm'):
        if request.POST.get('rm') == 'all':
            cart_obj.purchase_set.all().delete()
        else:
            Purchase.objects.filter(pk=request.POST.get('rm'), cart=cart_obj).delete()

    return render(request, 'shopping_cart/cart.html',
                  {
                    'cart': cart_obj
                  })
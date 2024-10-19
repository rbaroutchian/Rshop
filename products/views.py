from django.shortcuts import render, get_object_or_404
from products.models import Product

def index(request):
    return render(request, 'home_base.html')
def product_list(request):
    products = Product.objects.all().order_by('Ptitle')
    return render(request, 'product_moduels/product_list.html',
                  {'products': products})


# def product_detail(request, id):
#     selected_product = get_object_or_404(Product, id=id)
#     return render(request, 'product_moduels/product_detail.html',
#                   {'product': selected_product})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product_moduels/product_detail.html',
                  {'product': product})

def site_header_component(request):
    context = {
        'link': 'آموزشی'
    }
    return render(request, 'header_component.html', context)

def site_footer_component(request):
    return render(request, 'footer_component.html', {})

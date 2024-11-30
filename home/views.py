from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from products.models import Product, ProductCategory



# def index(request):
#     return render(request, 'home/home_page.html')

# in ravesh baraye enteghale data
class homeView(View):
    def get(self, request):
        product = Product.objects.all().order_by('Ptitle')
        product2 = Product.objects.all().order_by('Pcategory')

        return render(request, 'home/home_page.html',
                      {'products': product,
                       'categories': product2})








# class homeView(TemplateView):
#     template_name = 'home/home_page.html'

def site_header_home_component(request):
    return render(request, 'header_home_component.html')


def site_footer_home_component(request):
    return render(request, 'footer_home_component.html', {})

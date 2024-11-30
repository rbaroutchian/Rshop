from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from products.models import Product
from django.views.generic import ListView, DetailView

class productListView(ListView):
    template_name = 'product_moduels/product_list.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 1

    def get_queryset(self):
        base_query = super(productListView, self).get_queryset()
        data = base_query.filter(is_active=True)
        return data




# class productListView(TemplateView):
#     template_name = 'product_moduels/product_list.html'
#     def get_context_data(self, **kwargs):
#         product = Product.objects.all().order_by('Ptitle')[:5]
#         context = super(productListView, self).get_context_data(**kwargs)
#         context['products'] = product
#         return context



class productDetailView(DetailView):
    template_name = 'product_moduels/product_detail.html'
    model = Product



    # def get_context_data(self, **kwargs):
    #     context = super(productDetailView, self).get_context_data()
    #     slug = kwargs['slug']
    #     product = get_object_or_404(Product, slug=slug)
    #     context['product'] = product
    #     return context


# class productDetailView(TemplateView):
#     template_name = 'product_moduels/product_detail.html'
#     def get_context_data(self, **kwargs):
#         context = super(productDetailView, self).get_context_data()
#         slug = kwargs['slug']
#         product = get_object_or_404(Product, slug=slug)
#         context['product'] = product
#         return context





def index(request):
    return render(request, 'home_base.html')
# def product_list(request):
#     products = Product.objects.all().order_by('Ptitle')
#     return render(request, 'product_moduels/product_list.html',
#                   {'products': products})


# def product_detail(request, id):
#     selected_product = get_object_or_404(Product, id=id)
#     return render(request, 'product_moduels/product_detail.html',
#                   {'product': selected_product})

# def product_detail(request, slug):
#     product = get_object_or_404(Product, slug=slug)
#     return render(request, 'product_moduels/product_detail.html',
#                   {'product': product})

def site_header_component(request):
    context = {
        'link': 'آموزشی'
    }
    return render(request, 'header_component.html', context)

def site_footer_component(request):
    return render(request, 'footer_component.html', {})

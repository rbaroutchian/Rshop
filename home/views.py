from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from products.models import Product, ProductCategory
from site_moduel.models import Slider, SiteSetting, FooterLinkBox, FooterLink
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from order_module.models import Order, OrderDetail

# def index(request):
#     return render(request, 'home/home_page.html')

# in ravesh baraye enteghale data
# class homeView(View):
#     def get(self, request):
#         product = Product.objects.all().order_by('Ptitle')
#         product2 = Product.objects.all().order_by('Pcategory')
#
#         return render(request, 'home/home_page.html',
#                       {'products': product,
#                        'categories': product2})

class homeView(TemplateView):
    template_name = 'home/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sliders = Slider.objects.filter(is_active=True)
        context['sliders'] = sliders
        return context
def site_header(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    context = {
        'site_setting': setting
    }
    return render(request, 'header_component.html', context)

def site_footer(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    footer_link_boxes = FooterLinkBox.objects.all()
    for item in footer_link_boxes:
        var = item.footerlink_set
    context = {
        'site_setting': setting,
        'footer_link_boxes': footer_link_boxes,

    }
    return render(request, 'footer_home_component.html', context)



class AboutView(TemplateView):
    template_name = 'home/about_page.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        site_setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
        context['site_setting'] = site_setting
        return context

def site_header_home_component(request):
    return render(request, 'header_home_component.html')


def site_footer_home_component(request):
    return render(request, 'footer_home_component.html', {})



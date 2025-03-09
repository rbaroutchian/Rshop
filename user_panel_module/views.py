from django.contrib import messages
from django.http import HttpRequest, JsonResponse, HttpResponseBadRequest, Http404
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, ListView
from order_module.models import Order, OrderDetail
from django.template.loader import render_to_string

from account_module.models import User
from .form import EditProfileModelForm,ChangePasswordForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from order_module .models import OrderDetail, Order


# Create your views here.


@method_decorator(login_required, name='dispatch')
class UserPanelDashboardPage(TemplateView):
    template_name = 'user_dashboard.html'


@method_decorator(login_required, name='dispatch')
class EditUserProfilePage(View):
    def get(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_form = EditProfileModelForm(instance=current_user)
        context = {
            'form': edit_form,
            'current_user': current_user
        }
        return render(request, 'edit_profile_page.html', context)

    def post(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_form = EditProfileModelForm(request.POST, request.FILES, instance=current_user)
        if edit_form.is_valid():
            edit_form.save(commit=True)

        context = {
            'form': edit_form,
            'current_user': current_user
        }
        return render(request, 'edit_profile_page.html', context)


@method_decorator(login_required, name='dispatch')
class ChangePassword(View):
    def get(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        change_pass_form = ChangePasswordForm(instance=current_user)
        context = {
            'pass_form': change_pass_form,
            'current_user': current_user
        }
        return render(request, 'change_pass.html', context)

    def post(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        change_pass_form = ChangePasswordForm(request.POST, request.FILES, instance=current_user)
        if change_pass_form.is_valid():
            # change_pass_form.save(commit=True)
            user = change_pass_form.save(commit=False)
            user.set_password(change_pass_form.cleaned_data['password'])
            user.save()
        context = {
            'pass_form': change_pass_form,
            'current_user': current_user
        }
        return render(request, 'change_pass.html', context)



class AddressEditPage(View):
    def get(self, request: HttpRequest):
        current_user = request.user
        address_org = current_user.address_org
        other_addresses = [current_user.address2, current_user.address3,
                           current_user.address4, current_user.address5,
                           current_user.address6]
        context = {
            'address_org': address_org,
            'other_addresses': other_addresses
        }
        return render(request, 'address_page.html', context)

    def post(self, request):
        if not request.user.is_authenticated:
            messages.error(request, 'ابتدا وارد شوید.')
            return redirect('login_page')

        new_address = request.POST.get('address')
        if not new_address:
            messages.error(request, 'لطفا آدرس را وارد کنید.')
            return HttpResponseBadRequest('لطفا آدرس را وارد کنید.')

        user = request.user
        if not user.address_org:
            user.address_org = new_address
        elif not user.address2:
            user.address2 = new_address
        elif not user.address3:

            user.address3 = new_address
        elif not user.address4:
            user.address4 = new_address
        elif not user.address5:
            user.address5 = new_address
        elif not user.address6:
            user.address6 = new_address
        else:
            messages.error(request, 'تمام فیلدهای آدرس پر شده‌اند.')
            return redirect('edit_address_page')

        user.save()
        messages.success(request, 'آدرس با موفقیت ذخیره شد.')
        return redirect('edit_address_page')


@login_required
def user_panel_menu_component(request: HttpRequest):
    current_user = User.objects.filter(id=request.user.id).first()
    current_order, create = Order.objects.prefetch_related('orderdetails_set').get_or_create(is_paid=False,
                                                                                            user_id=request.user.id)
    total_count = 0
    for order_detail in current_order.orderdetails_set.all():
        total_count = order_detail.count
    context = {
        'user': current_user,
        'count': total_count
    }
    return render(request, 'components/user_panel_menu_component.html', context)


def user_basket(request: HttpRequest):
    current_order,create = Order.objects.prefetch_related('orderdetails_set').get_or_create(is_paid=False, user_id=request.user.id)
    total_amount = 0
    for order_detail in current_order.orderdetails_set.all():
        total_amount += order_detail.product.Pprice * order_detail.count

    context = {

        'order': current_order,
        'sum': total_amount,
        'page_title': 'سبد خرید'
    }
    return render(request, 'user_basket.html', context)


@login_required()
def remove_order_detail(request):
    detail_id=request.GET.get('detail_id')
    if detail_id is None:
        return JsonResponse({
            'status':'not_found_detail_id'
        })
    deleted_count, deleted_dict = OrderDetail.objects.filter(id=detail_id,order__is_paid=False,order__user_id=request.user.id).delete()
    if deleted_count == 0:
        return JsonResponse({
            'status': 'detail_not_found'
        })

    current_order, created = Order.objects.prefetch_related('orderdetails_set').get_or_create(is_paid=False, user_id=request.user.id)
    total_amount = current_order.calculate_total_price()
    context = {
        'order': current_order,
        'sum': total_amount,
    }
    return JsonResponse({
        'status': 'success',
        'body': render_to_string('user_panel_module/user_basket_content.html', context)
    })


def change_order_details_count(request):
    detail_id= request.GET.get('detail_id')
    state = request.GET.get('state')
    if detail_id is None or state is None:
        return JsonResponse({
            'status': 'not_found_detail_id'
        })
    order_details = OrderDetail.objects.filter(id=detail_id, order__user_id=request.user.id,
                                               order__is_paid=False).first()
    if order_details is None:
        return JsonResponse({
            'status': 'detail_not_found'
        })
    if state == 'increase':
        order_details.count += 1
        order_details.save()
    elif state == 'decrease':
        if order_details.count == 1:
            order_details.delete()
        else:
            order_details.count -= 1
            order_details.save()
    else:
        return JsonResponse({
            'status': 'state_invalid'
        })

    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid=False, user_id=request.user.id)
    total_amount = current_order.calculate_total_price()

    context = {
        'order': current_order,
        'sum': total_amount,
    }
    return JsonResponse({
        'status': 'success',
        'body': render_to_string('user_panel_module/user_basket_content.html',
                                 context)
    })


def my_shopping_detail(request: HttpRequest, order_id):
    order = Order.objects.prefetch_related('orderdetails_set__product').filter(id=order_id, user_id=request.user.id).first()
    if order is None:
        raise Http404('سبد خرید مورد نطر یافت نشد')
    return render(request, 'user_shopping_detail.html', context={
        'order': order
    })


@method_decorator(login_required, name='dispatch')
class MyShopping(ListView):
    model = Order
    template_name = 'user_shopping.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        requests: HttpRequest = self.request
        queryset = queryset.filter(user_id=requests.user.id, is_paid=True)
        return queryset

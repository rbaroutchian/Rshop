from django.shortcuts import render, redirect
from products.models import Product
from .models import Order, OrderDetail
from django.http import HttpRequest, JsonResponse
from django.contrib.auth.decorators import login_required
import requests
import json
import time
from django.conf import settings
from django.http import HttpRequest, HttpResponse

# Create your views here.
def add_product_to_order(request: HttpRequest):
    product_id = int(request.GET.get('product_id'))
    count = int(request.GET.get('count'))

    if count < 1:
        return JsonResponse({
            'status': 'invalid_count',
            'text':'مقدار وارد شده معتبر نیست',
            'confirm_button_text':'چشم',
            'icon':'warning'
        })



    if request.user.is_authenticated:
        product = Product.objects.filter(id=product_id, is_active=True, is_delete=False).first()
        if product is not None:
            current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
            current_order_detail = current_order.orderdetails_set.filter(product_id=product_id).first()
            if current_order_detail is not None:
                current_order_detail.count += count
                current_order_detail.save()
            else:
                new_detail = OrderDetail(order_id=current_order.id, product_id=product_id, count=count)
                new_detail.save()

            return JsonResponse({
                'status': 'success',
                'text': 'محصول مورد نظر با موفقیت به سبد خرید شما اضافه شد',
                'confirm_button_text': 'باشه ممنونم',
                'icon': 'success'
            })
        else:
            return JsonResponse({
                'status': 'not_found',
                'text': 'محصول مورد نظر یافت نشد',
                'confirm_button_text': 'چشم چک میکنم',
                'icon': 'error'
            })
    else:
        return JsonResponse({
            'status': 'not_logged_in',
            'text': 'برای افزودن به سبدخرید ابتدا باید وارد سایت شوید',
            'confirm_button_text': 'ورود به سایت',
            'icon': 'error'
        })

ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/"
# ZP_API_REQUEST = f"https://www.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
# ZP_API_VERIFY = f"https://www.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
# ZP_API_STARTPAY = f"https://www.zarinpal.com/pg/StartPay/"

amount = 1000
description = "نهایی کردن خرید شما از سایت ما"
phone = 'YOUR_PHONE_NUMBER'
CallbackURL = 'http://127.0.0.1:8000/verify_payment/'

# @login_required
# def request_payment(request: HttpRequest):
#     current_order, created = Order.objects.prefetch_related('orderdetails_set').get_or_create(is_paid=False, user_id=request.user.id)
#     total_price = 0
#     for order_detail in current_order.orderdetails_set.all():
#         total_price += order_detail.product.Pprice * order_detail.count
#
#
#     # total_price = current_order.calculate_total_price()
#     if total_price == 0:
#         return redirect(reverse('user-basket'))
#     req_data = {
#         'MerchantID': settings.MERCHANT,
#         'Amount': total_price *10,
#         'Callback_url': CallbackURL,
#         "Phone": phone,
#         'Description': description
#     }
#     req_header = {'accept': 'application/json', 'content-type': 'application/json'}
#     req = requests.post(url=ZP_API_REQUEST, data=json.dumps(req_data), headers=req_header)
#     authority = req.json()['data']['authority']
#     if len(req.json()['errors']) == 0:
#         return redirect(ZP_API_STARTPAY, format(authority=authority))
#     else:
#         e_code = req.json()['errors']['code']
#         e_message = req.json()['errors']['message']
#         return HttpRequest(f'Error code :{e_code}, Error Message: {e_message}')




@login_required
def request_payment(request: HttpRequest):
    try:
        current_order, created = Order.objects.prefetch_related('orderdetails_set').get_or_create(
            is_paid=False, user_id=request.user.id
        )

        total_price = sum(
            detail.product.Pprice * detail.count for detail in current_order.orderdetails_set.all()
        )

        if total_price == 0:
            return redirect(reverse('user-basket'))

        req_data = {
            'MerchantID': settings.MERCHANT,
            'Amount': total_price * 10,
            'CallbackURL': CallbackURL,
            'Description': f'پرداخت سفارش شماره {current_order.id}',
            'Mobile': request.user.profile.phone_number if hasattr(request.user, 'profile') else ''
        }

        req_header = {'accept': 'application/json', 'content-type': 'application/json'}
        response = requests.post(url=ZP_API_REQUEST, data=json.dumps(req_data), headers=req_header)
        response_data = response.json()
        if response.status_code == 200 and 'data' in response_data:
            authority = response_data['data'].get('authority')
            if authority:
                return redirect(f"{ZP_API_STARTPAY}{authority}")

        errors = response_data.get('errors', {})
        e_code = errors.get('code', 'Unknown code')
        e_message = errors.get('message', 'Unknown message')
        return HttpResponse(f'خطا در درخواست پرداخت: کد {e_code} - {e_message}')

    except Exception as e:
        return HttpResponse(f'خطای غیرمنتظره: {str(e)}')





@login_required
def verify_payment(request:HttpRequest):
    current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
    total_price = current_order.calculate_total_price()
    t_authority = request.GET['Authority']
    if request.GET.get('status') == 'ok':
        req_header = {'accept': 'application/json', 'content_type': 'application/json'}
        req_data = {
            'merchant_id': settings.MERCHANT,
            'amount': total_price*10,
            'authority': t_authority

        }
        req = request.post(url=ZP_API_VERIFY, data=json.dumps(req_data), headers=req_header)
        if len(req.json()['error']) == 0:
            t_status = req.json()['code']
            if t_status == 100 :
                current_order.is_paid = True
                current_order.payment_date=time.time()
                current_order.save()
                ref_str = req.json()['data']['ref_id']
                return render(request,'order_module/payment_result.html',{
                    'success': f'تراکنش شما با کد پیگیری{ref_str} با موفقیت انجام شد'
                })
            elif t_status == 101:
                return render(request, 'order_module/payment_result.html',{
                    'info':f'این تراکنش قبلا ثبت شده است'
                })
            else:
                return render(request, 'order_module/payment_result.html', {
                    'error': str(req.json()['data']['message'])
                })
        else:
            e_code = req.json()['error']['code']
            e_message = req.json()['error']['message']
            return render(request, 'order_module/payment_result.html',{
                'error':e_message
            })
    else:
        return render(request, 'order_module/payment_result.html',{
            'error':'پرداخت با خطا مواجه شد/کاربر از پرداخت ممانعت کرد'
        })


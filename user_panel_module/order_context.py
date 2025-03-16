from order_module.models import Order


def basket_context(request):
    context = {}
    if request.user.is_authenticated:
        current_order, created = Order.objects.prefetch_related('orderdetails_set').get_or_create(is_paid=False,
                                                                                                  user_id=request.user.id)
        total_amount = sum(
            order_detail.product.Pprice * order_detail.count
            for order_detail in current_order.orderdetails_set.all()
        )
        total_items = sum(order_detail.count for order_detail in current_order.orderdetails_set.all())

        context = {
            'basket_order': current_order,
            'basket_total': total_amount,
            'total_items': total_items
        }
    return context

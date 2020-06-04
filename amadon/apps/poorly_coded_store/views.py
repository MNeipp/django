from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    item = Product.objects.get(id=request.POST['item_id'])
    quantity_from_form = int(request.POST["quantity"])
    price = item.price
    total_charge = quantity_from_form * price
    print("Charging credit card...")
    recent_order = Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    request.session['recent_order_id'] = recent_order.id
    return redirect("/receipt")

def receipt(request):
    all_orders = Order.objects.all()
    total_items = 0
    total_spent = 0
    for order in all_orders:
        total_items += order.quantity_ordered
        total_spent += order.total_price
    context={
        "recent_order": Order.objects.get(id=request.session['recent_order_id']),
        "all_orders": Order.objects.all(),
        "total_items": total_items,
        "total_spent":total_spent,
    }
    return render(request, "store/checkout.html",context)

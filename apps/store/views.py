from django.shortcuts import render, redirect
products = [
    {'id': 1, 'name': 'Dojo Tshirt', 'price': 19.99},
    {'id': 2, 'name': 'Dojo Sweater', 'price': 24.99},
    {'id': 3, 'name': 'Dojo Cup', 'price': 4.99},
    {'id': 4, 'name': 'Algorithm Book', 'price': 49.99}
]

def index(request):
    if 'cart' not in request.session:
        request.session['cart'] = {'total': 0, 'items': 0, 'last_charge': 0}            
    context = { 'products': products }
    return render(request, 'store/index.html', context)

def add(request):
    if request.method == 'POST':
        qty = int(request.POST.get('qty'))
        item_id = int(request.POST.get('product_id'))
        item = filter(lambda product: product['id'] == item_id, products)[0]
        current_total = qty * item['price']
        request.session['cart']['items'] += int(request.POST.get('qty'))
        request.session['cart']['total'] += current_total
        request.session['cart']['last_charge'] = current_total
        request.session.modified = True
        return redirect('/store/checkout')

def cart(request):
    return render(request, 'store/cart.html')

from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    if request.GET.get('sort') == 'min_price':
            sort = 'price'
    elif request.GET.get('sort') == 'max_price':
            sort = '-price'
    else:
        sort = '-name'
    phones_object = Phone.objects.all().order_by(sort)
    context = {'phones': phones_object}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    print(slug)
    phone_obj = Phone.objects.filter(slug=slug)
    context = {'phone': phone_obj[0]}
    return render(request, template, context)

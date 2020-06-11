from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product


def Product_item(request):
    # p = Product(name='utuy', weight='237891', price='2348924')
    # p.save()
    if request.method == "POST":
        pname = request.POST.get('pname')
        weight = request.POST.get('weight')
        price = request.POST.get('price')
        print(price)
        p = Product(name=pname, weight=weight, price=price)
        p.save()
        # return redirect('/')
        return redirect('/login')
    else:
        return HttpResponse('404 - NOT FOUND ')
        # return render(request, 'create.htm')

    # else:
    # return HttpResponse('404 - NOT FOUND ')

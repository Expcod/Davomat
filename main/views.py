
from django.shortcuts import render, redirect
from . import models

def product_detail(request, id):
    product = models.Product.objects.get(id=id)
    categorys = models.Category.objects.all()
    recomendation = models.Product.objects.filter(
        category_id=product.category.id).exclude(id=product.id)[:3]
    images = models.ProductImage.objects.filter(product_id=product.id)
    is_saved = None

    context = {
        'product':product,
        'categorys':categorys,
        'recomendation':recomendation,
        'images':images,
        'range':range(product.review), # 0
        'range_passiv':range(5-product.review), # 5
        'is_saved':is_saved
    }
    return render(request, 'product/detail.html', context)

def create_staff(request):
    models.Staff.objects.create(
        user=request.user,
        product_id=request.GET['product_id'] # id
    )
    return redirect('main:index')


def list_staff(request):
    objects = models.Staff.objects.filter(user=request.user)






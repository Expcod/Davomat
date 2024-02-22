
from django.shortcuts import render, redirect
from . import models


def create_staff(request):
    models.Staff.objects.create(
        user=request.user,
        product_id=request.GET['product_id'] # id
    )
    return redirect('main:index')


def list_staff(request):
    objects = models.Staff.objects.filter(user=request.user)






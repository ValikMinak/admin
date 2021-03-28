from django.http import HttpResponse
from django.shortcuts import render

from main_admin.models import Product, Rating


class H:
    def process(self):
        print('H process()')


class A:
    # def process(self):
    #     print('A process()')
    pass


class B(A):
    # def process(self):
    #     print('B process()')
    pass


class C(B):
    # def process(self):
    #     print('С process()')
    pass


class D(C, H):
    pass


def get_mro(request):
    instance = Product.objects.create(name='lalalallala sd fasd', description='Descr', rating='e')
    a = instance
    return HttpResponse('<h1>Hey</h1>')

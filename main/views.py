# -*- coding: utf-8 -*-

from django.shortcuts import render
# Create your views here.


def index(request):
    context = dict()
    context['ip'] = request.META.get(u'REMOTE_ADDR', u'Unknown')
    if request.method == 'GET':
        try:
            sum = int(request.GET.get('a', 0))
            sum += int(request.GET.get('b', 0))
            context['sum'] = sum
        except ValueError:
            pass
    return render(request, u'main/index.html', context)
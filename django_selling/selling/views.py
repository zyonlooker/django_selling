from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger

from .models import Free, Half

def base(request):
    return render(request, 'selling/base.html')

def free(request):
    free_item_list = Free.objects.all()
    paginator = Paginator(free_item_list, 5)
    page = request.GET.get('page')
    try:
        free_item_list_single = paginator.page(page)
    except PageNotAnInteger:
        free_item_list_single = paginator.page(1)
    except (EmptyPage, InvalidPage):
        free_item_list_single = paginator.page(paginator.num_pages)
    return render(request, 'selling/free.html', {'free_item_list_single': free_item_list_single})

def half(request):
    half_item_list = Half.objects.all()
    paginator = Paginator(half_item_list, 5)
    page = request.GET.get('page')
    try:
        half_item_list_single = paginator.page(page)
    except PageNotAnInteger:
        half_item_list_single = paginator.page(1)
    except (EmptyPage, InvalidPage):
        half_item_list_single = paginator.page(paginator.num_pages)
    return render(request, 'selling/half.html', {'half_item_list_single': half_item_list_single})

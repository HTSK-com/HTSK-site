from django.shortcuts import render
from portfolio.models import Works


def home_page(request):
    """Домашняя страница"""
    return render(request, 'index.html')


def our_works_page(request):
    """Страница с работами нашей компании"""
    items = Works.objects.order_by('-id')
    for i in range(len(items)):
        items[i].photo_path.name = '/'.join(items[i].photo_path.name.split('/')[1:])
    return render(request, 'our_works.html', {'items': items})

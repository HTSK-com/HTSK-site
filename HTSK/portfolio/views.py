from django.shortcuts import render


def home_page(request):
    """Домашняя страница"""
    return render(request, 'index.html')


def our_works_page(request):
    """Страница с работами нашей компании"""
    return render(request, 'our_works.html')

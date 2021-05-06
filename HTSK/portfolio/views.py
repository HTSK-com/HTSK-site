from django.shortcuts import render

from portfolio.models import Works, Employee


def home_page(request):
    """Домашняя страница"""
    return render(request, 'home.html')


def our_works_page(request):
    """Страница с работами нашей компании"""
    items = Works.objects.order_by('-id')
    for i in range(len(items)):
        items[i].photo_path.name = '/'.join(items[i].photo_path.name.split('/')[1:])
    return render(request, 'our_works.html', {'items': items})


def about_us(request):
    """Страница о нас"""
    return render(request, 'about_us.html')


def employees(request):
    """Страница о наших сотрудниках"""
    items = Employee.objects.all()
    for i in range(len(items)):
        items[i].picture_of_staff.name = '/'.join(items[i].picture_of_staff.name.split('/')[1:])
    return render(request, 'employees.html', {'items': items})


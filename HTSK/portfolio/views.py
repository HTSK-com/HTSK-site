from django.shortcuts import render, redirect

from portfolio.models import Works, Employee
from .froms import OrderForm

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


def one_employee(request, employee_id):
    """Страница с подробной информацией о каждом сотруднике"""
    item = Employee.objects.get(id=employee_id)
    item.picture_of_staff.name = '/'.join(item.picture_of_staff.name.split('/')[1:])
    return render(request, 'employee.html', {'item': item})


def make_an_order(request):
    error = ''
    if request.method == 'POST':
        form = OrderForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Неверная форма'
    form = OrderForm()
    return render(request, 'make_an_order.html', {'form': form, 'error': error})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from decimal import Decimal
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')

from .models import Staff
from django.contrib.auth.decorators import login_required

# @login_required
# def dashboard(request):
#     staff, created = Staff.objects.get_or_create(user=request.user)
#     # use 'staff' instead of 'waiter' if you renamed the variable
#     return render(request, 'dashboard.html', {'staff': staff})


# @login_required
# def dashboard(request):
#     staff, created = Staff.objects.get_or_create(user=request.user)

#     # Fetch all tables and reservations
#     total_tables = Table.objects.all()
#     reservations = Reservation.objects.all()

#     # Create a dictionary of reserved tables (table number -> reservation)
#     reserved_tables = {int(r.table_number): r for r in reservations}

#     return render(request, 'dashboard.html', {'staff': staff,'total_tables': total_tables,'reserved_tables': reserved_tables,'reservations': reservations})

@login_required
def dashboard(request):
    waiter = Staff.objects.get(user=request.user)
    # waiter = get_object_or_404(Staff, user=request.user)
    reservations = Reservation.objects.filter(waiter=waiter)
    return render(request, 'dashboard.html', {'reservations': reservations})

# @login_required
# def create_reservation(request):
#     if request.method == 'POST':
#         table = request.POST['table_number']
#         waiter = Staff.objects.get(user=request.user)
#         Reservation.objects.create(table_number=table, waiter=waiter)
#         return redirect('dashboard')
#     return render(request, 'create_reservation.html')
# #
# from django.shortcuts import render, redirect
# from .models import Reservation
# from datetime import datetime

# def create_reservation(request):
#     if request.method == 'POST':
#         table_number = request.POST.get('table_number')
#         Reservation.objects.create(table_number=table_number, reserved_at=datetime.now())
#         return redirect('create_reservation')

#     # Umumiy 10 ta stol bor deb olaylik (1 dan 10 gacha)
#     total_tables = range(1, 11)
#     reserved_tables = Reservation.objects.values_list('table_number', flat=True)

#     return render(request, 'create_reservation.html', {
#         'total_tables': total_tables,
#         'reserved_tables': reserved_tables,
#     })

# 





# from django.shortcuts import render, redirect
# # from .models import Reservation, Table, Staff  # Import Staff model (for waiters)
# from .models import Reservation, Staff  # Use the correct model name

# def create_reservation(request):
#     if request.method == "POST":
#         table_number = request.POST.get('table_number')
#         waiter_id = request.POST.get('waiter_id')

#         # Create a new reservation entry
#         reservation = Reservation.objects.create(
#             table_number=table_number,
#             waiter=Staff.objects.get(id=waiter_id)  # Reference to Staff model (Waiter)
#         )
#         return redirect('order_detail', res_id=reservation.id)  # Redirect to a success page
    
#     staff_members = Staff.objects.all()  # Get all staff members (waiters)
#     return render(request, 'create_reservation.html', {'staff_members': staff_members})

# from django.shortcuts import render, redirect
# from .models import Reservation, Staff, Table  # Make sure to import the Table model

# def create_reservation(request):
#     staff_members = Staff.objects.all()  # Get all staff members (waiters)

#     if request.method == "POST":
#         table_number = request.POST.get('table_number')
#         waiter_id = request.POST.get('waiter_id')

#         # Create a new reservation entry
#         reservation = Reservation.objects.create(
#             table_number=table_number,
#             waiter=Staff.objects.get(id=waiter_id)  # Reference to Staff model (Waiter)
#         )

#         # Redirect to the order detail page after creating the reservation
#         return redirect('order_detail', res_id=reservation.id)

#     total_tables = Table.objects.all()  # Get all tables
#     reserved_tables = Reservation.objects.values_list('table_number', flat=True)  # Get all reserved table numbers

#     # Pass the context variables to the template
#     return render(request, 'create_reservation.html', {
#         'staff_members': staff_members,
#         'total_tables': total_tables,
#         'reserved_tables': reserved_tables
#     })

from django.shortcuts import render, redirect
from .models import Reservation, Staff, Table

def create_reservation(request):
    staff_members = Staff.objects.all()

    if request.method == "POST":
        table_number = request.POST.get('table_number')
        waiter_id = request.POST.get('waiter_id')

        reservation = Reservation.objects.create(
            table_number=table_number,
            waiter=Staff.objects.get(id=waiter_id)
        )
        return redirect('order_detail', res_id=reservation.id)

    total_tables = Table.objects.all()
    reservations = Reservation.objects.select_related('waiter')
    #reserved_tables = {int(r.table_number): r for r in reservations}

    return render(request, 'create_reservation.html', {
        'staff_members': staff_members,
        'total_tables': total_tables,
        #'reserved_tables': reserved_tables
    })



# from django.shortcuts import render, redirect
# from .models import Reservation, Staff

# def create_reservation(request):
#     if request.method == 'POST':
#         table_number = request.POST.get('table_number')
#         waiter_id = request.POST.get('waiter_id')
#         if waiter_id:
#             waiter = Staff.objects.get(id=waiter_id)
#             Reservation.objects.create(table_number=table_number, waiter=waiter)
#             return redirect('create_reservation')
#         else:
#             return render(request, 'create_reservation.html', {'error': 'Please select a waiter.'})

#     total_tables = range(1, 11)
#     reservations = Reservation.objects.all()  # Fetch all reservations
#     reserved_tables = {r.table_number: r for r in reservations}  # Dict: table_number -> Reservation object
#     waiters = Staff.objects.all()

#     return render(request, 'create_reservation.html', {
#         'total_tables': total_tables,
#         'reserved_tables': reserved_tables,
#         'waiters': waiters,
#     })

# def table_status(request):
#     total_tables = Table.objects.all()
#     reserved_tables = Reservation.objects.all()
#     return render(request, 'table_status.html', {
#         'total_tables': total_tables,
#         'reserved_tables': reserved_tables
#     })
# def table_status(request):
#     total_tables = Table.objects.all()
#     reservations = Reservation.objects.select_related('waiter')
#     reserved_tables = {int(r.table_number): r for r in reservations}
#     return render(request, 'table_status.html', {
#         'total_tables': total_tables,
#         'reserved_tables': reserved_tables
#     })


from django.shortcuts import render
from .models import Reservation, Table

from collections import defaultdict

def table_status(request):
    total_tables = Table.objects.all()
    reservations = Reservation.objects.select_related('waiter')
    
    reserved_tables = defaultdict(list)
    for r in reservations:
        reserved_tables[int(r.table_number)].append(r)

    return render(request, 'table_status.html', {
        'total_tables': total_tables,
        'reserved_tables': reserved_tables
    })

# def table_status(request):
#     total_tables = Table.objects.all()
#     reservations = Reservation.objects.select_related('waiter')
#     reserved_tables = {int(r.table_number): r for r in reservations}  # This stores reserved tables

#     # Make sure you pass both 'total_tables' and 'reserved_tables' to the template
#     return render(request, 'table_status.html', {
#         'total_tables': total_tables,
#         'reserved_tables': reserved_tables
#     })

from django.shortcuts import render, get_object_or_404
from .models import Reservation

def table_reservations(request, table_number):
    reservations = Reservation.objects.filter(table_number=table_number)
    return render(request, 'table_reservations.html', {
        'table_number': table_number,
        'reservations': reservations
    })

def mark_done(request, reservation_id):
    if request.method == 'POST':
        reservation = get_object_or_404(Reservation, id=reservation_id)
        reservation.delete()  # yoki reservation.status = 'done' bo'lishi mumkin
        return redirect('dashboard')


# def order_view(request, table_id):
#     table = Table.objects.get(id=table_id)
#     reservation = Reservation.objects.filter(table=table).first()
#     return render(request, 'order.html', {'reservation': reservation})

# In waiterapp/views.py
# from django.shortcuts import render, get_object_or_404
# from .models import Reservation, Table, Staff
#  # Adjust based on your model

# def order_detail(request, res_id):
#     total_tables = Table.objects.all()  # Masalan, barcha jadvallarni olish
#     reserved_tables = Reservation.objects.values_list('table_number', flat=True)  # Rezervatsiya qilingan jadvallarni olish
#     context = {
#         'res_id' : res_id,
#         'total_tables': total_tables,
#         'reserved_tables': reserved_tables,
#     }
#     return render(request, 'order.html', context)
# from django.shortcuts import render, get_object_or_404
# from .models import MenuItem,Reservation, Table, Order

# def order_detail(request, res_id):
#     reservation = get_object_or_404(Reservation, id=res_id)
#     menu = MenuItem.objects.all()
#     total_tables = Table.objects.all()
#     reserved_tables = Reservation.objects.values_list('table_number', flat=True)

#     context = {
#         'reservation': reservation,  # Add this line
#         'menu': menu,
#         'res_id': res_id,
#         'total_tables': total_tables,
#         'reserved_tables': reserved_tables,
#         # 'orders': ...,  # If you're also using orders in template, don't forget this
#     }
#     return render(request, 'order.html', context)
# from django.shortcuts import render, get_object_or_404
# from .models import Menu, Reservation, Table, Order

# def order_detail(request, res_id):
#     reservation = get_object_or_404(Reservation, id=res_id)
#     menu = Menu.objects.all()
#     total_tables = Table.objects.all()
#     reserved_tables = Reservation.objects.values_list('table_number', flat=True)
#     orders = Order.objects.filter(reservation=reservation)

#     context = {
#         'reservation': reservation,
#         'menu': menu,
#         'res_id': res_id,
#         'total_tables': total_tables,
#         'reserved_tables': reserved_tables,
#         'orders': orders,  # Bu HTMLdagi order jadvali uchun kerak
#     }
#     return render(request, 'order.html', context)



# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Reservation, Menu, Order

# def order_detail(request, res_id):
#     reservation = get_object_or_404(Reservation, id=res_id)
#     menu = Menu.objects.all()  # Menu ro'yxatini olish
#     orders = Order.objects.filter(reservation=reservation)  # Mavjud buyurtmalarni olish

#     if request.method == "POST":
#         menu_item_id = request.POST.get("menu_item")  # Foydalanuvchi tanlagan taomni olish
#         quantity = request.POST.get("quantity")  # Foydalanuvchi tanlagan miqdorni olish

#         # Menu item va quantity ni olish
#         menu_item = Menu.objects.get(id=menu_item_id)
#         order = Order(reservation=reservation, menu_item=menu_item, quantity=quantity)
#         order.save()  # Buyurtmani saqlash

#         return redirect('order_detail', res_id=reservation.id)  # Buyurtmalar sahifasiga qaytish

#     context = {
#         'reservation': reservation,
#         'menu': menu,
#         'orders': orders,  # Mavjud buyurtmalarni ko'rsatish
#     }

#     return render(request, 'order.html', context)

from django.shortcuts import render, get_object_or_404
from .models import Reservation  # or the model related to the order

def order_view(request, id):
    # Assuming you are handling the reservation or order with this ID
    reservation = get_object_or_404(Reservation, id=id)
    # Add any additional context if necessary
    return render(request, 'order.html', {'reservation': reservation})

def order_detail(request, res_id):
    reservation = get_object_or_404(Reservation, id=res_id)
    menu = Menu.objects.all()  # Get all menu items
    orders = Order.objects.filter(reservation=reservation)  # Get existing orders

    if request.method == 'POST':
        # Get menu item and quantity from the form
        menu_item_id = request.POST.get('menu_item')
        quantity = request.POST.get('quantity')

        # Ensure valid data is provided
        if menu_item_id and quantity:
            menu_item = get_object_or_404(Menu, id=menu_item_id)
            order = Order(reservation=reservation, menu_item=menu_item, quantity=quantity)
            order.save()  # Save the order
            return redirect('order_detail', res_id=reservation.id)  # Redirect to the order page

    context = {
        'reservation': reservation,
        'menu': menu,
        'orders': orders,
    }

    return render(request, 'order.html', context)


# def order_detail(request, res_id):
#     table = get_object_or_404(Table, id=res_id)
#     return render(request, 'order.html', {'table': table})

# @login_required
# def order_view(request, reservation_id):
#     reservation = Reservation.objects.get(id=reservation_id)
#     menu = Menu.objects.all()
#     orders = Order.objects.filter(reservation=reservation)

#     if request.method == 'POST':
#         item_id = request.POST['menu_item']
#         quantity = int(request.POST['quantity'])
#         item = Menu.objects.get(id=item_id)
#         Order.objects.create(reservation=reservation, menu_item=item, quantity=quantity)
#         return redirect('order_view', reservation_id=reservation_id)

#     return render(request, 'order.html', {'menu': menu, 'orders': orders, 'reservation': reservation})
@login_required
def bill_view(request, reservation_id):
    reservation = Reservation.objects.get(id=reservation_id)
    orders = Order.objects.filter(reservation=reservation)
    subtotal = sum(order.get_price() for order in orders)
    service_charge = subtotal * Decimal('0.15')
    total = subtotal + service_charge

    return render(request, 'bill.html', {
        'reservation': reservation,  # <== bu qatorni qo‘sh
        'orders': orders,
        'subtotal': subtotal,
        'service_charge': service_charge,
        'total': total
    })

from django.shortcuts import get_object_or_404

from django.shortcuts import redirect, get_object_or_404
from .models import Order

def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()  # Buyurtmani o'chirish
    return redirect('order_detail', res_id=order.reservation.id)  # Buyurtmalar sahifasiga qaytish

# @login_required
# def cancel_order(request, order_id):
#     order = get_object_or_404(Order, id=order_id)
#     reservation_id = order.reservation.id
#     order.delete()
#     return redirect('order_view', reservation_id=reservation_id)

# # In waiterapp/views.py


from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create_reservation/', views.create_reservation, name='create_reservation'),
    path('bill/<int:reservation_id>/', views.bill_view, name='bill_view'),
    path('cancel_order/<int:order_id>/', views.cancel_order, name='cancel_order'),
    path('order_detail/<int:res_id>/', views.order_detail, name='order_detail'),
    path('order/<int:id>/', views.order_view, name='order_view'),
    path('table_status/', views.table_status, name='table_status'),
    path('table/<int:table_number>/reservations/', views.table_reservations, name='table_reservations'),
    path('reservation/<int:reservation_id>/done/', views.mark_done, name='mark_done'),
]
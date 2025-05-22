from django.db import models

from django.db import models
from django.contrib.auth.models import User

# class Staff(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

#     is_waiter = models.BooleanField(default=False)

from django.db import models

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Reservation(models.Model):
    table_number = models.IntegerField()
    reserved_at = models.DateTimeField(auto_now_add=True)
    waiter = models.ForeignKey(Staff, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Table {self.table_number} - {self.waiter}"

class Menu(models.Model):
    name = models.CharField(max_length=100)
    
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name} - ${self.price}"

# class Reservation(models.Model):
#     table_number = models.IntegerField()
#     waiter = models.ForeignKey(Staff, on_delete=models.CASCADE)
#     reserved_at = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_price(self):
        return self.menu_item.price * self.quantity

from django.db import models

# class Table(models.Model):
#     table_number = models.IntegerField(unique=True)
#     seats = models.IntegerField()
#     is_reserved = models.BooleanField(default=False)

#     def __str__(self):
#         return f"Table {self.table_number}"
# waiterapp/models.py

from django.db import models

class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    seats = models.IntegerField(default=4)
    is_reserved = models.BooleanField(default=False)

    def __str__(self):
        return f"Table {self.table_number}"


# 💡 Shu yerdayoq yaratish funksiyasi:
def create_default_tables():
    for i in range(1, 16):
        Table.objects.create(table_number=i, seats=4)

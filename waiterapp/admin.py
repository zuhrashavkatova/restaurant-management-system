from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Staff,Reservation,Table
from .models import Menu




admin.site.register(Staff)
admin.site.register(Menu)
admin.site.register(Reservation)
admin.site.register(Table)
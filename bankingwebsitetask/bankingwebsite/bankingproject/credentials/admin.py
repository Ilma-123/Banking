from django.contrib import admin
from .models import Customer, Account

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'contact_number')
    search_fields = ('username', 'email')

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_number', 'customer', 'account_type', 'balance')
    list_filter = ('account_type',)
    search_fields = ('account_number', 'customer__username', 'customer__email')



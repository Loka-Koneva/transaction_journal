from django.contrib import admin
from .models import Stock, Currency


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    pass


@admin.register(Currency)
class CurrensyAdmin(admin.ModelAdmin):
    pass

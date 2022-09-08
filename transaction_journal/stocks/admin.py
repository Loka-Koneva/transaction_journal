from django.contrib import admin
from .models import (
    ETF,
    Bond,
    Share,
    Stock,
    Currency,
    TargetForDate,
    PriceTarget
)


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    pass


@admin.register(Currency)
class CurrensyAdmin(admin.ModelAdmin):
    pass


admin.site.register(ETF)
admin.site.register(Bond)
admin.site.register(Share)
admin.site.register(TargetForDate)
admin.site.register(PriceTarget)

from django.contrib import admin
from .models import Expense,Incomes
# Register your models here.
# admin.site.register(Expense)
admin.site.register(Incomes)


# Register your models here.
# admin.site.register(Expense)
@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('text','date','amount', 'user')
    list_filter = ('text','user')
    search_fields = ('text',)
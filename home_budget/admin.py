from django.contrib import admin

from .models import Subcategory, Category, Expense, Income

# Register your models here.
@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_filter = ("category", )
    search_fields = ('subcategory', )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("category", )
 
@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    search_fields = ('category',)
    autocomplete_fields = ['category', 'subcategory']
    list_display = ('month','category', 'subcategory', 'provide_amount', 'real_amount', )

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    pass
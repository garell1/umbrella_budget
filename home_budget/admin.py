from django.contrib import admin

from .models import Subcategory, Category, Expense, Income

# Register your models here.
@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    pass

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    pass
from django.shortcuts import render
from django.views.generic import DetailView

from .models import Category, Subcategory, Expense, Income

# Create your views here.
class SummaryView(DetailView):
    model = Expense
    template_name = 'summary.html'


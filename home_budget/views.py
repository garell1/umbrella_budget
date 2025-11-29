from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import DetailView, ListView
from django.views.decorators.clickjacking import xframe_options_exempt
from django.utils.decorators import method_decorator

from .models import Expense, Income

# Create your views here.
class IndexView(TemplateView):
    template_name = "home_budget/index.html"
    
    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex["expenses"] = Expense.objects.all()

        return contex
    

@method_decorator(xframe_options_exempt, name='dispatch')
class SummaryView(ListView):
    model = Expense
    template_name = 'home_budget/include/summary.html'
    context_object_name = "expenses"
    

@method_decorator(xframe_options_exempt, name='dispatch')
class IncomeView(DetailView):
    model = Income
    template_name = "home_budget/include/income.html"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        base_query = self.model.objects.all()
        
        context["income"] = base_query
        return context
         

@method_decorator(xframe_options_exempt, name='dispatch')
class HousingView(ListView):
    model = Expense
    template_name = "home_budget/include/housing.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_query = self.model.objects.all()
        
        context["house"] = base_query.filter(category=11)
        context["transport"] = base_query.filter(category=9)
        context["insurence"] = base_query.filter(category=10) 

        return context


@method_decorator(xframe_options_exempt, name='dispatch')
class FinanseMgmtView(ListView):
    model = Expense
    template_name = "home_budget/include/finance_mgmt.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_query = self.model.objects.all()
        
        context["credits"] = base_query.filter(category=6)
        context["taxes"] = base_query.filter(category=5)
        context["law"] = base_query.filter(category=7) 

        return context

@method_decorator(xframe_options_exempt, name='dispatch')
class LivingCostView(ListView):
    model = Expense
    template_name = "home_budget/incluide/living_cost.html"


@method_decorator(xframe_options_exempt, name='dispatch')
class FamilyCareView(ListView):
    model = Expense
    template_name = "home_budget/include/family_care.html"
    

@method_decorator(xframe_options_exempt, name='dispatch')
class YearReportView(ListView):
    model = Expense
    template_name = "home_budget/include/year_report.html"

    #def get_queryset(self):
    #    home_objects = model.objects.filter(month__year=slug_month)
    #    return super().get_queryset()
    
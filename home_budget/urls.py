from django.urls import path
#from django.views.generic import TemplateView

from .views import (
    IndexView,
    SummaryView, 
    IncomeView,
    HousingView,
    FinanseMgmtView,
    LivingCostView,
    FamilyCareView
) 

urlpatterns = [
    path("", IndexView.as_view(), name="index" ),
    path("summary/", SummaryView.as_view(), name="summary" ),
    path("income/", IncomeView.as_view(), name="income" ),
    path("housing/", HousingView.as_view(), name="housing" ),
    path("finanse-mgmt/", FinanseMgmtView.as_view(), name="finanse" ),
    path("living-cost/", LivingCostView.as_view(), name="living_cost" ),
    path("Family-care/", FamilyCareView.as_view(), name="family_care" ),
]

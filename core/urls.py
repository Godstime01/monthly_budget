from django.urls import path
from django.views.generic import TemplateView, FormView

from .forms import Budget, BudgetCreationForm
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('dashboard/', views.DashboardView.as_view(template_name='dashboard.html'), name='dashboard'),
    path("dashboard/<str:category>/", views.filter_expenses, name='filter'),
    path("reset-account/", views.reset_account, name='reset-account'),
    path('update-expense/<str:pk>/', views.update_expense, name='edit_expense'),
    path('delete-expense/<str:pk>/', views.ExpenseDelete.as_view(), name='delete_expense'),
    
]
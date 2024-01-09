from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.views.generic import CreateView, FormView, UpdateView, DeleteView
from django.shortcuts import redirect, render

from .models import Expense, Budget
from .forms import ExpenseCreationForm, BudgetCreationForm


class HomePageView(CreateView):
    model = Budget
    template_name = 'index.html'
    form_class = BudgetCreationForm
    success_url = '/dashboard'

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        has_budget = request.session.get('has_budget', False)
        print("GEt", has_budget)

        if has_budget:
            return redirect('dashboard')
        return super().get(request, *args, **kwargs)
    
    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        print('form invalud')
        return super().form_invalid(form)
    
    def post(self, request, *args, **kwargs):
        print('called post')
        session_key = request.session.session_key

        if not session_key:
            request.session.save()
            session_key = request.session.session_key

        request.session['has_budget'] = True
        print(request.session.get('has_budget'))

        form = self.get_form()
        form.instance.session_id = session_key
        print(form.instance.session_id)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form: Any) -> HttpResponse:

        print('form valid')
        return super().form_valid(form)


class DashboardView(FormView):
    model = Expense
    form_class = ExpenseCreationForm
    template_name = 'dashboard.html'
    success_url = '/dashboard'

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        has_budget = request.session.get('has_budget', False)
        # print("GEt", has_budget)

        if not has_budget:
            return redirect('/')

        # check if user is filtering
        
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        session_key = self.request.session.session_key

        qs = Budget.objects.filter(session_id=session_key)[0]
        print(qs)
        context = super().get_context_data()
        context['budget'] = qs
        return context
    
    def form_valid(self, form: Any):
        budget = Budget.objects.filter(session_id = self.request.session.session_key)[0]

        print(f'Form vaild{budget}')
        form.instance.budget = budget
        form.save()

        return super().form_valid(form)
    

def update_expense(request, pk):

    expense = Expense.objects.filter(pk = pk)[0]
    form = ExpenseCreationForm(instance = expense)

    if request.method == 'POST':
        form = ExpenseCreationForm(request.POST)

        if form.is_valid():
            form.save()

    print(expense)

    return render(request, 'partials/edit_modal.html', {'form': form})

class ExpenseDelete(DeleteView):
    model = Expense
    template_name = 'expenses.html'
    success_url = '/dashboard'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return HttpResponse(status=204)

def filter_expenses(request, category=None):
    if category is not None:
        print("reach")
        qs = category
        print(qs)
        budget = Budget.objects.filter(session_id = request.session.session_key)[0]

        expenses = budget.expense_set.filter(category=qs)
        print(expenses)

    return render(request, 'partials/filter_expenses.html', {'expenses': expenses})

def reset_account(request):
    if request.method == 'POST':
        # Delete the session
        print('session deleted')
        request.session.flush()
    return redirect('/')

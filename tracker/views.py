from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ExpenseForm
from .models import Expense


class ExpenseCreateAndListView(LoginRequiredMixin,CreateView):
    template_name ='expense_list.html'
    form_class = ExpenseForm
    model = Expense
    success_url = reverse_lazy('expense')

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Expense.objects.filter(user=self.request.user)
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        expense = form.save(commit=False)
        expense.user = self.request.user
        expense.save()
        return super().form_valid(form) 


class ExpenseDetailView(LoginRequiredMixin,DetailView):
    template_name = 'expense_detail.html'
    model = Expense
    context_object_name = 'expense'

class ExpenseUpdateView(LoginRequiredMixin,UpdateView):
    template_name = 'modal_form.html'
    form_class = ExpenseForm
    model = Expense

class ExpenseDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'delete_confirm.html'
    model = Expense
    success_url = reverse_lazy('view_expense')

# class ExpenseListView(LoginRequiredMixin, ListView):
#     model = Expense
#     template_name = 'expense_list.html'
#     search_fields = ['title', 'description']
#     paginate_by = 20 
#     def get_queryset(self):
#         return Expense.objects.filter(user=self.request.user)

#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data(**kwargs)
#     #     #context['fields'] = [field.name for field in self.model._meta.get_fields()]
#     #     context['fields'] = ['title','image','cost']
#     #     context['update_url'] = 'edit_expense'
#     #     context['delete_url'] = 'delete_expense'
#     #     return context
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .forms import ExpenseForm
from .models import Expense



class ExpenseCreateView(CreateView):
    template_name ='generic_form.html'
    form_class = ExpenseForm
    model = Expense
    success_url = reverse_lazy('view_expense')
    
    def get_initial(self):
        initial = super().get_initial().copy()
        initial['user'] = self.request.user.id
        return initial

    # def form_valid(self, form):
    #     expense = form.save(commit=False)
    #     expense.user = self.request.user
    #     expense.save()
    #     return super().form_valid(form) 

class ExpenseUpdateView(UpdateView):
    template_name = 'generic_form.html'
    form_class = ExpenseForm
    model = Expense

class ExpenseDeleteView(DeleteView):
    template_name = 'delete_confirm.html'
    model = Expense
    success_url = reverse_lazy('view_expense')

class ExpenseListView(ListView):
    model = Expense
    template_name = 'generic_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['fields'] = [field.name for field in self.model._meta.get_fields()]
        context['fields'] = ['title','image','cost']
        context['update_url'] = 'edit_expense'
        context['delete_url'] = 'delete_expense'
        return context
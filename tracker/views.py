from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView, View, MonthArchiveView,FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ExpenseForm, DateRangeForm
from .models import Expense
from django.utils.encoding import smart_str

from django.http import HttpResponse
from wsgiref.util import FileWrapper
from io import StringIO
from .utils import dump
from django.utils.timezone import now

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
    success_url = reverse_lazy('expense')

class DownloadCsv(LoginRequiredMixin, FormView):
    form_class = DateRangeForm
    template_name = 'modal_form.html'

    def post(self, request, *args, **kwargs):
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        out_file = StringIO()
        qs = Expense.objects.filter(user=request.user, bill_date__range= [start_date, end_date])
        dump(qs, out_file)
        out_file.seek(0, 0)
        print(out_file.getvalue())
        response = HttpResponse(FileWrapper(out_file), content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename=%s' % smart_str('CSVData.csv')
        return response  
    
class ExpenseMonthArchiveView(MonthArchiveView):
    date_field = 'bill_date'
    allow_future = True
    template_name = 'expense_archive_month.html'
    
    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)
        
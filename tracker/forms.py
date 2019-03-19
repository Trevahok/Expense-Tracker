from . models import Expense
from django import forms
class ExpenseForm(forms.ModelForm):
    
    class Meta:
        model = Expense
        fields = '__all__'
        widgets= {
            'user': forms.HiddenInput(),
            'bill_date': forms.DateInput(attrs={'class': 'datepicker'}),
            'bill_time': forms.TimeInput(format='%H:%M')
        }

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from tagulous.models import TagField
# Create your models here.

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User', help_text='Choose the User to whom this expense belongs to')
    title = models.CharField(verbose_name='Title', max_length=100, help_text='A brief title of the expense')
    image = models.ImageField(blank=True, null=True,verbose_name='Image', upload_to='expense_image/', max_length=16384, help_text='Upload an Image')
    cost = models.PositiveSmallIntegerField(verbose_name='Expenditure Cost', help_text='Enter the Amount Expended')
    description = models.TextField(blank=True,verbose_name='Description', help_text='Enter the Description for the type of expense')
    bill_date = models.DateField(default=now, verbose_name='Bill Date')
    bill_time = models.TimeField(default=now, verbose_name='Billing Time')
    created = models.DateTimeField(verbose_name='Created Date', auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(verbose_name='Modified Date', auto_now=True, auto_now_add=False)
    tags = TagField(force_lowercase=True)

    def __str__(self):
        return f'{self.title} {self.cost} {self.bill_date}'
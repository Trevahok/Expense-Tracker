from django.urls import path
from . import views
urlpatterns = [

   path('expense/', views.ExpenseListView.as_view(), name='view_expense') ,
   path('expense/add', views.ExpenseCreateView.as_view(), name='add_expense') ,
   path('expense/<pk>/edit', views.ExpenseUpdateView.as_view(), name='edit_expense'),
   path('expense/<pk>/delete', views.ExpenseDeleteView.as_view(), name='delete_expense'),
]

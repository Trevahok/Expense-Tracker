from django.urls import path
from . import views
urlpatterns = [

   path('expense/<pk>/', views.ExpenseDetailView.as_view(), name='view_expense'),

   path('', views.ExpenseCreateAndListView.as_view(), name='expense') ,
   path('expense/<pk>/edit', views.ExpenseUpdateView.as_view(), name='edit_expense'),
   path('expense/<pk>/delete', views.ExpenseDeleteView.as_view(), name='delete_expense'),
]

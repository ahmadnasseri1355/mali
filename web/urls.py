from django.urls import path
from .views import submit_expense

urlpatterns = [
    path('submit/expense/',submit_expense, name='submit_expense'),
]

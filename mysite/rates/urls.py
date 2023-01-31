from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('bank/<int:bank_id>/', branches, name='branches'),
]

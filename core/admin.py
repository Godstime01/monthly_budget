from django.contrib import admin
from .models import Expense, Budget

admin.site.register([Expense, Budget])
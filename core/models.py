from django.db import models

# Create your models here.
class Budget(models.Model):
    income = models.DecimalField(decimal_places = 2, max_digits=10)
    name = models.CharField(max_length=20, unique=True)
    goal = models.CharField(max_length=200)
    start_date = models.DateTimeField(auto_now_add=True)
    session_id = models.CharField(max_length=100, null=True, unique=True)

    def get_user_expenses(self):
        return self.expense_set.all()
    
    def get_total_expenses(self):
        return sum(
            [expense.amount for expense in self.get_user_expenses()]
            )
    
    def get_available_amount(self):
        return self.income - self.get_total_expenses()

    def __str__(self):
        return self.name 
    

class Expense(models.Model):
    CATEGORY = (
        ('debt', 'DEBT'),
        ('food', 'FOOD'),
        ('hobbies', 'HOBBIES'),
        ('rent', 'RENT'),
        ('saving', 'SAVING'),
        ('medication', 'MEDICATION'),
        ('subscription', 'SUBSCRIPTION'),
        ('others', 'OTHERS')
    )

    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=12, choices = CATEGORY)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    budget = models.ForeignKey('Budget', on_delete=models.CASCADE)


    def __str__(self):
        return self.name
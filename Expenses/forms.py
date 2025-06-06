from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['date', 'category', 'amount', 'description']

class UploadCSVForm(forms.Form):
    csv_file = forms.FileField()
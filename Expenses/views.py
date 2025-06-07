from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm, UploadCSVForm
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from datetime import datetime
import csv, io

@login_required
def dashboard(request):
    month = request.GET.get('month')
    expenses = Expense.objects.filter(user=request.user)

    if month:
        expenses = expenses.filter(date__month=month)

    summary = expenses.values('category').annotate(total=Sum('amount'))
    return render(request, 'dashboard.html', {'summary': summary, 'month': month})

@login_required
def add_expense(request):
    form = ExpenseForm(request.POST or None)
    if form.is_valid():
        expense = form.save(commit=False)
        expense.user = request.user
        expense.save()
        return redirect('dashboard')
    return render(request, 'add_expense.html', {'form': form})

@login_required
def upload_csv(request):
    if request.method == 'POST':
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            decoded_file = csv_file.read().decode('utf-8')
            io_string = io.StringIO(decoded_file)
            for row in csv.reader(io_string, delimiter=',', skipinitialspace=True):
                try:
                    date_str, category, amount, *desc = row
                    Expense.objects.create(
                        user=request.user,
                        date=datetime.strptime(date_str, "%Y-%m-%d").date(),
                        category=category,
                        amount=float(amount),
                        description=' '.join(desc) if desc else ''
                    )
                except Exception as e:
                    print(f"Error processing row {row}: {e}")
            return redirect('dashboard')
    else:
        form = UploadCSVForm()
    return render(request, 'upload_csv.html', {'form': form})

def home(request):
    return render(request, 'home.html')
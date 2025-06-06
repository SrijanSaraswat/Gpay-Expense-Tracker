# GPay Expense Tracker

This is a Django-based personal expense tracker inspired by the design and functionality of Google Pay's monthly insights. It allows users to upload expenses via CSV, categorize their spending, and visualize monthly data through a clean dashboard interface.

## Features

- User authentication (registration, login, logout)
- Expense entry via form or CSV upload
- Categorization of expenses (canteen, hotel, transport, recharge, stationery, others)
- Monthly and category-wise summary of expenses
- Interactive dashboard using Chart.js
- Filtering of expenses by category and month
- Responsive and modern user interface styled to resemble Google Pay

<p> <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" /> <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" /> <img src="https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white" /> <img src="https://img.shields.io/badge/Chart.js-F5788D?style=for-the-badge&logo=chartdotjs&logoColor=white" /> <img src="https://img.shields.io/badge/DRF-Django%20REST%20Framework-ff1709?style=for-the-badge&logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" /> <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" /> <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" /> </p>
## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/gpay-expense-tracker.git
cd gpay-expense-tracker
```

### 2. Create a virtual environment and activate it

```bash
# On Windows
python -m venv env
env\Scripts\activate

# On macOS/Linux
python3 -m venv env
source env/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, manually install:

```bash
pip install django djangorestframework django-crispy-forms
```

### 4. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser (admin)

```bash
python manage.py createsuperuser
```

### 6. Start the development server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

## Usage Overview

- Login or register as a user
- Navigate to the dashboard to view current month’s summary
- Use the Add Expense form to manually log a transaction
- Use the Upload CSV page to bulk upload expenses
- Expenses are categorized and summarized for the selected month
- Interactive bar chart provides visual insights

## CSV Format for Upload

Ensure your CSV is structured as follows:

```
date,category,amount,description
2025-05-01,canteen,120,Lunch
2025-05-03,transport,50,Bus fare
...
```

## API Endpoints (Optional Extension)

The project is REST-ready. If enabled:

- `/api/expenses/` - List and create expenses
- `/api/upload/` - CSV upload via API
- `/api/summary/?month=5` - Monthly/category summary

## Folder Structure

```
Gpay_Expense_Tracker/
├── Expenses/
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── dashboard.html
│   │   ├── add_expense.html
│   │   └── upload_csv.html
│   ├── admin.py
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   └── urls.py
├── Gpay_Expense_Tracker/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
└── manage.py
```

## License

This project is provided for educational and personal use only.


# 💸 GPay Expense Tracker

A Django-based expense tracker inspired by Google Pay’s monthly insights. Upload your CSV, add expenses, and analyze where your money goes. Designed for students and professionals who want simple, intuitive financial clarity.

---

## 🚀 Features

- 📤 Upload CSV bank statements
- 📝 Add expenses manually
- 📊 Dashboard with categorized insights
- 🔍 Filter and search your expenses
- 🗓️ Monthly summary similar to Google Pay
- 🔐 Login functionality (basic auth)
- 🧠 Simple and responsive UI using Bootstrap

---

## 🛠️ Tech Stack

- **Framework:** Django
- **Language:** Python
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite
- **Charts:** Coming soon (Chart.js / Plotly)

---

## 🗂️ Project Structure

```
Gpay_Expense_Tracker/
│
├── Expenses/                   # Main app
│   ├── migrations/
│   ├── templates/              # HTML files (dashboard, login, etc.)
│   │   ├── base.html
│   │   ├── dashboard.html
│   │   ├── login.html
│   │   ├── add_expense.html
│   │   └── upload_csv.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── Gpay_Expense_Tracker/       # Django config folder
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3                  # Local SQLite DB
├── manage.py                   # Django CLI utility
└── README.md                   # Project overview
```

---

## 🖼️ Screenshots

Dashboard              |  Upload CSV            |  Add Expense
:---------------------:|:----------------------:|:----------------------:
![Dashboard](screenshots/dashboard.png) | ![Upload](screenshots/upload.png) | ![Add Expense](screenshots/add_expense.png)

---

## ▶️ How to Run

```bash
git clone https://github.com/SrijanSaraswat/Gpay-Expense-Tracker.git
cd Gpay-Expense-Tracker

# Create virtual environment
python -m venv env
env\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt

# Run the server
python manage.py runserver
```

Visit: `http://127.0.0.1:8000/`

---

## 📌 To-Do

- [ ] Add charts to dashboard
- [ ] Export expense summary as PDF
- [ ] Add category-wise filters and graphs
- [ ] Deploy on Render / Vercel

---

## 📄 License

MIT License

---

## 👨‍💻 Author

[Srijan Saraswat](https://github.com/SrijanSaraswat)

# Django Expense Tracker

A web-based personal finance tracking system built with Django and Bootstrap 5.  
Upload expenses via CSV, view monthly summaries, and analyze your spending by category.

---

## Features

- User Authentication (Login/Logout)
- Upload Expenses via CSV
- Filter by Month and Category
- Monthly Summary Table View
- REST API Endpoints (CRUD + Summaries)
- Bootstrap 5 Responsive UI
- PostgreSQL-ready (uses SQLite by default)
- Deployment-ready for Render/Heroku

---

## Quick Start

### 🔧 Prerequisites

- Python 3.8+
- PostgreSQL (optional)
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/SrijanSaraswat/django-expense-tracker.git
cd django-expense-tracker

# Create virtual environment
python -m venv venv
source venv/bin/activate        # On Linux/Mac
venv\Scripts\activate         # On Windows

# Install dependencies
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file in the root directory:

```ini
DJANGO_SECRET_KEY=your-secret-key
DEBUG=True
```

> You must install `python-dotenv` and import it in `settings.py` to load this.

---

## Database Setup

```bash
# Apply migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser
```

---

## Running the Server

```bash
python manage.py runserver
```

Open your browser at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Sample CSV Format

Below is the required format for uploading expenses via `/upload/`:

```csv
date,category,amount,description
2025-05-01,canteen,150,Lunch
2025-05-03,transport,100,Auto fare
```

---

## API Endpoints

| Endpoint                    | Method | Description               |
|-----------------------------|--------|---------------------------|
| `/api/expenses/`            | GET    | List all expenses         |
| `/api/expenses/`            | POST   | Add new expense           |
| `/api/expenses/<id>/`       | GET    | Retrieve a single expense |
| `/api/expenses/<id>/`       | PUT    | Update an expense         |
| `/api/expenses/<id>/`       | DELETE | Delete an expense         |
| `/api/expenses/summary/`    | GET    | Category summary by month |

---

## Project Structure

```
django-expense-tracker/
├── expenses/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── serializers.py
│   ├── api_views.py
│   └── ...
├── expense_tracker/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── templates/
├── static/
├── .env.example
├── .gitignore
├── requirements.txt
└── manage.py
```

---

## Development

### Code Formatting

```bash
black .
flake8
```

---

## Deployment

### Render (Recommended)

- Create new Web Service
- Connect to GitHub repo
- Set environment variables
- Use `gunicorn expense_tracker.wsgi` as start command

### Heroku (Optional)

```bash
heroku create
heroku addons:create heroku-postgresql:hobby-dev
git push heroku main
heroku run python manage.py migrate
```

---

## License

This project is licensed under the MIT License.  
See `LICENSE` for details.

---

## Author

**Srijan Saraswat**  
📧 Email: saraswatsrijan@email.com  
🔗 Project Repo: [https://github.com/SrijanSaraswat/django-expense-tracker](https://github.com/SrijanSaraswat/django-expense-tracker)

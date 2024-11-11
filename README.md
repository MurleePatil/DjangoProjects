# Clinicals - Patient Management and Clinical Data Analysis

**Clinicals** is a Django-based web application for managing patient data and clinical information. The application allows users to add, update, and delete patient records, as well as store and analyze clinical data.

---

## Features

- **Add Patients**: Allows healthcare professionals to add new patient records, including personal details, medical history, and contact information.
- **Update Patient Information**: Modify existing patient records as necessary (e.g., change personal details or medical history).
- **Delete Patients**: Remove patient records from the system.
- **Add Clinical Data**: Store clinical data such as test results, medical observations, etc.
- **Clinical Data Analysis**: Analyze and generate reports on clinical data for research or clinical decision-making.

---

## Requirements

To run the **Clinicals** application, you will need the following:

- Python 3.8 or higher
- pip (Python package manager)
- Django 4.x or higher (install using pip)
- mysqlclient (install using pip)
- MySQL 8.x or compatible (alternatively, you can use PostgreSQL, but the default is MySQL)


---

## Installation

### Clone the Repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/MurleePatil/clinicals.git
cd clinicals
```

### Set Up the Database

Ensure you have MySQL installed and running on your system. You can download it from [MySQL’s official site](https://dev.mysql.com/downloads/).

Next, create a database for the application in MySQL:

```sql
CREATE DATABASE clinicalsdb;
```

### Configure the Database in Django

In your `settings.py` file (found in the `clinicals` directory), configure the database settings to use MySQL. Locate the `DATABASES` setting and modify it to match your MySQL credentials:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'clinicalsdb',  # Name of the database you created
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### Apply Migrations

Run the following command to set up the database tables:

```bash
python manage.py migrate
```

### Run the Development Server

Start the development server with the following command:

```bash
python manage.py runserver
```

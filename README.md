# FossAlgo
A website to keep track of CP contests of Foss community members.

This project is built with:

- **Python**: version 3.x
- **Django**: version 3.x or 4.x
- **Database**: MySQL

## Setup

### Prerequisites

Make sure you have the following installed on your machine:

- Python 3.x
- Django
- [Any other tools like `pip`, `virtualenv`]

### Installation

Follow these steps to set up the project on your local machine:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/praptisharma28/FossAlgo.git
   cd FossAlgo
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```
Please include virtual enviornment in gitignore file, do not commit it.

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. Access the project in your browser at `http://127.0.0.1:8000`.

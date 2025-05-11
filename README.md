# Blog Website

A simple blog website built with Django. Users can read and write blog posts, and the site is dynamically managed.

## Project Structure
blog/ # Blog-related code
home/ # Home-related views
iCoder/ # Personal website or portfolio
templates/ # HTML templates
db.sqlite3 # SQLite database
manage.py # Django management
requirements.txt # Project dependencies
README.md # Project description



## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AshimPoudelInpl/Blog_Website.git
   cd Blog_Website
Set up a virtual environment and activate it:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
Install dependencies:


pip install -r requirements.txt
Apply migrations:


python manage.py migrate
Run the development server:


python manage.py runserver
Now visit http://127.0.0.1:8000/ in your browser.

Technologies:
Django
SQLite
HTML/CSS

This concise version covers the basics of the project setup and usage.

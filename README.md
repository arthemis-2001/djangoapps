This is a repo with two Django applications in it. The first application is a simple portfolio and the second one is a realtime My Little Pony-themed chat.

## Technologies used
Portfolio:
- Python 3.12
- Django 5.0
- HTML for templates
- Bootstrap 3 for CSS

## Prerequisites
- Python 3.xx
- PIP

## Installation

```bash
   git clone https://github.com/arthemis2001/djangoapps.git
   cd https://github.com/arthemis2001/djangoapps.git
   python3 -m venv .env
   source .env/bin/activate
   pip3 install -r requirements.txt
   ```

## Portfolio
First, you need to set up the database used by Django app:
```bash
python manage.py migrate
```

The main Django database model is PortfolioItem, which represents a project listed in the portfolio and has following fields:
1. Title
2. Description
3. Image
4. URL to the project
5. Likes

There are sample data in `example_database.json` file that you can use to test the app. Load it into the app using:
```bash
python manage.py loaddata example_database.json
```

Run the app with 
```bash
python manage.py runserver
```

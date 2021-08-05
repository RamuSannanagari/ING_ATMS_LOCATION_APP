# ING_ATMS_LOCATION_APP


# OVERVIEW
This Flask application contains the basic user management functionality ( login) to demonstrate how to develop and test a Flask project using Flask,Sqlite,pytest.
Applications list out all ATM Location detais for Dutch City



# How to Run
In the top-level directory:
python app.py


# Installation Instructions

#Pull down the source code from this GitLab repository:
git clone 

cd flask_user_management_example

pip install -r requirements.txt

python app.py

Navigate to 'http://localhost:7197/login' to view the website!


Key Python Modules Used

Flask: micro-framework for web application development
pytest: framework for testing Python projects
Jinga2 - templating engine
SQLAlchemy - ORM (Object Relational Mapper)

Testing
To run all the tests:
python -m pytest -v
python -m pytest --cov-report term-missing --cov=middleware

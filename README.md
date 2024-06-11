Online Judge

The Online Judge project is a web-based platform designed to facilitate coding competitions, practice problems, and algorithm challenges. This project allows users to submit their code, receive instant feedback on their submissions, and engage in competitive programming.

Built-From

Backend: Django for handling the web application logic and database interactions
Frontend: HTML, CSS, Bootstrap and python inbuilt templates ( like Jinja)
Database: SQLite3 from Python Inbuilt libraries
Containerization: Docker for easy deployment and environment consistency.

Description

Online Judge is a comprehensive web application designed to offer a platform for coding enthusiasts to solve and submit programming problems. Built using Django, this platform enables users to practice their coding skills, and engage with a community of developers.

Key Features

1) Problem Repository: Browse a wide range of problems categorized by difficulty, topic, and programming language.
2) Code Submission: Submit code solutions in multiple programming languages and receive instant feedback on performance and correctness.
3) Real-time Judging: Solutions are automatically judged against predefined test cases, providing immediate results.
4) User Accounts: Register and log in to track your progress, save submissions, and view your submission history.
5) Custom Testing: Run your code with custom input to test and debug before final submission.
6) User Profiles: Manage your account, view your solved problems, and track your performance statistics.

Key Components

a) Home App:
The home app is the heart of the Online Judge project. It includes the following key components:

1) Models (models.py): Define the database schema, including models for Users, Problems, Submissions, and more.
2) Views (views.py): Handle the request-response logic for the application, including rendering templates and processing form data.
3) Forms (forms.py): Define the forms used in the application, such as user registration, problem creation, and code submission.
4) Templates (templates/): Contains HTML templates for rendering the web pages. This includes pages for problem listings, submission details, user profiles, and more.
5) Media (media/) : Contains images used across the application.
6) URLs (urls.py): Route incoming requests to the appropriate views.
   
b) Online_Judge App:
The online_judge project directory contains global settings and configurations for the Django project.

1) Settings (settings.py): Configuration settings for the Django project, including database settings, installed apps, middleware, and more.
2) URLs (urls.py): Define the URL patterns for the project, linking to the URLs defined in the home app.
3) WSGI (wsgi.py): Entry point for WSGI-compatible web servers to serve the Django project.

Installation & Set-up

Steps:
1) Clone the Repository
2) Setup Virtual Environment 
3) Install Dependencies (use requirements.txt)
4) Database Setup (if you are not using python's default sqlite3)
5) Apply Migrations (py manage.py makemigrations and py manage.py migrate)
6) Create superuser (py manage.py createsuperuser)
7) Run the Server (py manage.py runserver)
8) Access the application (Open your web browser and go to http://127.0.0.1:8000.)

Docker Setup

1) Build Image (using Dockerfile)
2) Run Docker Container (by mapping docker conatainer to your local port)
3) Access the Application (Open your web browser and go to http://127.0.0.1:8000.)

Usage

Navigating the Application

a) Home: Overview of the platform and latest updates.
b) Problems: Browse and select problems to solve.
c) Submissions: View your past submissions and their results.
d) Custom Test: Run custom tests on your code.
e) Profile: Manage your account, view stats, and update profile picture.

Submitting Code

i) Navigate to the "Problems" section.

ii) Select a problem to view its details.

iii) Write your solution in the provided code editor.

iv) Submit your code to see the results.

Running Custom Tests

i) Navigate to the "Custom Test" section.

ii) Select your programming language.

iii) Write or paste your code and input data.

iv) Run the code to see the output.

Contributing: 
We welcome contributions from the community! To contribute:

i) Fork the repository.

ii) Create a new branch.

iii) Make your changes and commit them.

iv) Push your changes to your fork.

v) Submit a pull request.


Author

Devansh Srivastava 
Devansh30032004 (github_username)


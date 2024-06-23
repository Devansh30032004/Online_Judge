# Online Judge Project

## Project Overview

The Online Judge project is a web-based platform designed to facilitate coding competitions, practice problems, and algorithm challenges. This project allows users to submit their code, receive instant feedback on their submissions, and engage in competitive programming.

## Built-From

- **Backend:** Django for handling the web application logic and database interactions
- **Frontend:** HTML, CSS, Bootstrap, and Python inbuilt templates (like Jinja)
- **Database:** SQLite3 from Python Inbuilt libraries
- **Containerization:** Docker for easy deployment and environment consistency

## Description

Online Judge is a comprehensive web application designed to offer a platform for coding enthusiasts to solve and submit programming problems. Built using Django, this platform enables users to practice their coding skills and engage with a community of developers.

## Key Features

- **Problem Repository:** Browse a wide range of problems categorized by difficulty, topic, and programming language.
- **Code Submission:** Submit code solutions in multiple programming languages and receive instant feedback on performance and correctness.
- **Real-time Judging:** Solutions are automatically judged against predefined test cases, providing immediate results.
- **User Accounts:** Register and log in to track your progress, save submissions, and view your submission history.
- **Custom Testing:** Run your code with custom input to test and debug before final submission.
- **User Profiles:** Manage your account, view your solved problems, and track your performance statistics.

## Key Components

### Home App

The home app is the heart of the Online Judge project. It includes the following key components:

- **Models (models.py):** Define the database schema, including models for Users, Problems, Submissions, and more.
- **Views (views.py):** Handle the request-response logic for the application, including rendering templates and processing form data.
- **Forms (forms.py):** Define the forms used in the application, such as user registration, problem creation, and code submission.
- **Templates (templates/):** Contains HTML templates for rendering the web pages, including pages for problem listings, submission details, user profiles, and more.
- **Media (media/):** Contains images used across the application.
- **URLs (urls.py):** Route incoming requests to the appropriate views.

### Online_Judge App

The online_judge project directory contains global settings and configurations for the Django project.

- **Settings (settings.py):** Configuration settings for the Django project, including database settings, installed apps, middleware, and more.
- **URLs (urls.py):** Define the URL patterns for the project, linking to the URLs defined in the home app.
- **WSGI (wsgi.py):** Entry point for WSGI-compatible web servers to serve the Django project.

## Installation & Set-up

1. Clone the Repository
2. Setup Virtual Environment
3. Install Dependencies (use requirements.txt)
4. Database Setup (if you are not using Python's default SQLite3)
5. Apply Migrations (`py manage.py makemigrations` and `py manage.py migrate`)
6. Create superuser (`py manage.py createsuperuser`)
7. Run the Server (`py manage.py runserver`)
8. Access the application (Open your web browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000))

## Docker Setup

1. Build Image (using Dockerfile)
2. Run Docker Container (by mapping Docker container to your local port)
3. Access the Application (Open your web browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000))

## Usage

### Navigating the Application

- **Home:** Overview of the platform and latest updates.
- **Problems:** Browse and select problems to solve.
- **Submissions:** View your past submissions and their results.
- **Custom Test:** Run custom tests on your code.
- **Profile:** Manage your account, view stats, and update profile picture.

### Submitting Code

1. Navigate to the "Problems" section.
2. Select a problem to view its details.
3. Write your solution in the provided code editor.
4. Submit your code to see the results.

### Running Custom Tests

1. Navigate to the "Custom Test" section.
2. Select your programming language.
3. Write or paste your code and input data.
4. Run the code to see the output.

## Contributing

We welcome contributions from the community! To contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request.

## Author

**Devansh Srivastava**

GitHub: [Devansh30032004](https://github.com/Devansh30032004)

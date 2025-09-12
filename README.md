## Claims Management System

## Overview
This project is a full-stack web application designed to manage and analyze insurance claims. It provides a dynamic, user-friendly interface for viewing claim data, adding annotations, and flagging items for review. The system is built with a modern tech stack focused on a server-rendered architecture, enhanced with HTMX for a responsive, single-page-application feel without the complexity of a large JavaScript framework.

This application was built as a solution to the company's full-stack developer challenge, implementing all core requirements and bonus features.

## Tech Stack
The application is built using the following technologies:

**Backend:** Python with Django (v4+)

**Database:** SQLite (lightweight, file-based)

**Frontend:** HTML5, CSS3

**Dynamic Frontend Logic:** HTMX & Alpine.js

**Styling:** Custom CSS for a modern, professional look



## Features

### Core Requirements
**Data Ingestion:** A custom management command (`load_claims_data`) ingests initial claim data from provided CSV files directly into the SQLite database.
**Claims List View:** A clean, paginated table displays all claims, showing key information like patient name, billed amount, paid amount, status, and insurer.
**Live Search & Filter:** The claims list can be filtered in real-time by insurer name and claim status. As the user types or selects a filter, the table updates instantly without a page reload.
**HTMX Detail View:** Clicking the "View" button on any claim dynamically loads a detailed view below the row, showing additional data like CPT codes and denial reasons without refreshing the page.
**Flag & Annotate:** Users can flag claims for review and add custom, timestamped notes to any claim. All annotations are stored in the database.


### Bonus Features Implemented
**Full User Authentication:** A complete and secure system allows users to register, log in, and log out. All notes and flags are linked to the specific user who created them, fulfilling the "user-specific annotations" requirement.
**Admin Dashboard:** A dedicated dashboard page at `/dashboard` provides high-level statistics, including the total number of flagged claims and the average underpayment calculated across the entire dataset.
**Advanced CSV Re-upload:** The data ingestion command was enhanced with `--mode` arguments, allowing data to be either completely overwritten or appended to the existing dataset.


## Setup and Installation
To run this project locally, please follow these steps:

### 1. Prerequisites

* Python 3.8+
* `pip` (Python package installer)

### 2. Clone the Repository

Clone this project to your local machine.

* git clone <your-repository-url>
* cd <project-folder>

### 3. Create and Activate a Virtual Environment

It's best practice to create a virtual environment to manage dependencies.

Create the environment
* python -m venv venv

Activate it (on Windows)
* .\venv\Scripts\Activate.ps1

Activate it (on macOS/Linux)
* source venv/bin/activate

### 4. Install Dependencies
Install Django and other required packages.
* pip install django pytz

### 5. Set Up the Database
Run the migrations to create the database tables.

* python manage.py makemigrations
* python manage.py migrate

### 6. Create a Superuser
Create an admin account to manage the application and test admin-specific features.

* python manage.py createsuperuser

Follow the prompts to create a username and password.

### 7. Load Initial Data
Use the custom management command to load the sample claims data into the database. Make sure your `claim_list_data.csv` and `claim_detail_data.csv` files are in a `data/` folder in the project root.

* python manage.py load_claims_data

### 8. Run the Development Server
You are now ready to run the application.

* python manage.py runserver

The application will be available at **`http://127.0.0.1:8000/`**.


## How to Use the Application

1.  **Login:** The application is secure and requires a login. Upon visiting the site, you will be directed to the login page. Use the superuser credentials you created, or sign up as a new user.
2.  **View Claims:** After logging in, you will see the main claims list.
3.  **Search and Filter:** Use the search bar and status dropdown to filter the claims in real-time.
4.  **View Details:** Click the "View" button on any claim to expand its detailed view.
5.  **Add Notes & Flag:** In the detail view, use the "Quick Actions" panel to add notes or flag a claim for review.
6.  **Visit Dashboard:** Click the "View Dashboard" link in the header to see aggregate statistics.

Claims Management System
A full-stack web application built with Django and HTMX for efficient insurance claim analysis and management. This project was developed as a solution to the ERISA Recovery Full-Stack Developer Challenge, implementing all core requirements and bonus features.

✨ Live Demo & Walkthrough

For a detailed walkthrough of the features, please watch the demo video:

https://drive.google.com/file/d/13IXARzylbwzxuuelI8HeEbRxcMoe9s8l/view?usp=sharing

A brief animation showcasing the application's features.

🚀 Core Features
This application provides a robust set of tools for claims analysts, built for speed and efficiency.

🔐 Secure User Authentication: A complete registration and login system ensures that all actions are secure and tied to a specific user. The session ends on the browser close for enhanced security.

📊 Dynamic Claims Dashboard: A high-level dashboard provides key statistics, including the total number of flagged claims and the average underpayment amount across the entire dataset.

⚡ Live Search & Filtering: The main claims list features a powerful live search that filters by insurer name and claim status as you type, updating the results instantly without page reloads.

📄 HTMX-Powered Detail View: Clicking on any claim fetches and displays a detailed information panel inline, preserving the user's context and scroll position.

✍️ User-Specific Annotations: Logged-in users can add timestamped notes to any claim. Notes created by admin users are specially marked for easy identification.

🚩 Claim Flagging: Users can flag claims for review with a single click. The UI provides instant visual feedback by displaying a flag icon on the main list.

📥 Flexible Data Ingestion: A custom Django management command handles loading the initial dataset from CSV files, with support for both overwriting and appending new data.

🛠️ Technology Stack
This project leverages a modern, server-rendered architecture to deliver a fast and responsive user experience.

Category

Technology

Backend

Python with Django

Database

SQLite

Frontend

HTMX for dynamic UI updates & Alpine.js for client-side interactivity

Styling

Custom CSS3 for a clean, professional, and fully responsive design.

Timezones

JavaScript Intl API & Django Middleware for automatic, user-specific time zone detection and display.

⚙️ Getting Started
To run this project locally, please follow these steps.

1. Prerequisites
Python 3.8+

pip (Python package installer)

2. Clone the Repository
git clone <your-repository-url>
cd claims_project

3. Set Up a Virtual Environment
It is highly recommended to use a virtual environment.

# Create the environment
python -m venv venv

# Activate on Windows
.\venv\Scripts\Activate.ps1

# Activate on macOS/Linux
source venv/bin/activate

4. Install Dependencies
pip install django pytz

5. Initialize the Database
This will create the database schema based on the models.

python manage.py makemigrations
python manage.py migrate

6. Create an Admin Account
Create a superuser account to access the Django Admin and test admin-specific features.

python manage.py createsuperuser

7. Load the Sample Data
Use the custom management command to populate the database from the provided CSV files. (Ensure your CSV files are in a data/ folder at the project root).

python manage.py load_claims_data

8. Run the Application
python manage.py runserver

The application will be running at http://127.0.0.1:8000/. You will be automatically redirected to the login page.

👤 Application Flow
Login/Register: Users must first log in or create a new account via the signup page.

View Claims List: After logging in, users are presented with a paginated list of all insurance claims.

Search & Analyze: Users can filter the list in real-time or click "View" to load detailed information for a specific claim.

Annotate & Flag: In the detail view, users can add notes or flag the claim. All actions are recorded with their username and a timestamp.

View Dashboard: Admins and users can navigate to the dashboard to see high-level analytics.

Logout: Logging out ends the session and securely redirects the user back to the login page.

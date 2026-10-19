📝 Notespace – Personal Note Management System

Notespace is a web-based Note Management System built using Python and Flask. It helps users securely create, organize, view, edit, search, and delete their personal notes through a simple and user-friendly interface.

🚀 Features

User Registration: Create an account to access your personal workspace.

Email OTP Verification: Verify your email address during registration.

Secure Login: Authenticate users before accessing their notes.

Create Notes: Save ideas, reminders, and important information.

View Notes: Open and read saved notes.

Edit Notes: Update existing notes whenever needed.

Delete Notes: Remove notes that are no longer required.

Search Notes: Find notes quickly.

User Profile: Access your personal profile.

Password Reset: Recover access to your account.

Responsive UI: Clean interface for a better user experience.

🛠️ Tech Stack

Backend: Python, Flask

Frontend: HTML, CSS, JavaScript

Database: As configured in the project

Email Service: SMTP using Gmail

Version Control: Git and GitHub

📂 Project Structure

Note_Management/
│
├── app.py
├── emailsend.py
├── utility.py
├── requirements.txt
├── setup.py
├── README.md
│
├── database/
│   ├── connection.py
│   └── tables.py
│
└── templates/
    ├── base.html
    ├── home.html
    ├── login.html
    ├── register.html
    ├── verifyotp.html
    ├── verify_reset_otp.html
    ├── reset_password.html
    ├── dashboard.html
    ├── add_notes.html
    ├── edit_note.html
    ├── view_notes.html
    └── profile.html

⚙️ Installation and Setup

1. Clone the repository

git clone https://github.com/jawaharvanapall1/Note_Management.git

2. Navigate to the project directory

cd Note_Management

3. Install dependencies

pip install -r requirements.txt

4. Configure email credentials

Set your Gmail address and Gmail App Password as environment variables. Never store email credentials directly in your source code.

Windows PowerShell:

$env:EMAIL_ADDRESS="your-email@gmail.com"
$env:EMAIL_APP_PASSWORD="your-gmail-app-password"

Replace the example values with your own credentials.

5. Configure the database

Configure your database connection according to the settings in the project's database connection file.

6. Run the application

python app.py

Open the local URL shown in your terminal. For example:

http://127.0.0.1:5004

🔐 Security

Keep email credentials and secret keys out of the repository.

Use environment variables for sensitive configuration.

Do not commit database files containing personal information.

Use HTTPS and production-safe settings when deploying the application.

🎯 Project Objective

The objective of Notespace is to provide a simple and secure platform for managing personal notes while demonstrating practical skills in Python, Flask, database integration, email verification, and web application development.

👨‍💻 Author

Jawahar Vanapalli

GitHub: @jawaharvanapall1

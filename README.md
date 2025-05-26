# Ayist Group Dashboard

Ayist Group Dashboard is a role-based web application built using Flask. It provides tailored user interfaces and features based on specific roles such as Admin, HR, Finance, and Superadmin.

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup](#setup)
- [Usage](#usage)
- [How to Change User Role](#how-to-change-user-role)
- [Directory Structure](#directory-structure)
- [Localization](#localization)
- [License](#license)

---

## Features

- **Role-Based Access Control**: Tailored dashboards and features for Admin, HR, Finance, and Superadmin roles.
- **Dynamic Dashboards**: Real-time data showcasing employee activities, projects, invoices, and company stats.
- **Multi-Language Support**: Built-in localization with English and Polish translations.
- **HR Dashboard**: Displays recent employee activities, onboarding progress, and HR stats.
- **Finance Dashboard**: Provides financial overviews, including income, expenses, and profit.
- **Customizable Navigation**: Dynamic menu based on user roles.
- **Project Summaries**: Track project progress, status, and client information.

---

## Tech Stack

- **Backend**: Python (Flask)
- **Frontend**: HTML5, Tailwind CSS, JavaScript
- **Environment Management**: `dotenv` for environment variables
- **Localization**: Flask-Babel
- **Icons**: Font Awesome

---

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Alyyyy88/ayist-group-task.git
   cd app
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the root directory and add:
     ```
     FLASK_APP=app.py
     FLASK_ENV=development
     SECRET_KEY=your_secret_key
     ```

5. Run the development server:
   ```bash
   flask run
   ```
   Access the application at `http://localhost:5000`.

---

## Usage

### Key Routes:
- **Set Language**: `/set_language/<lang_code>` (e.g., `/set_language/en` or `/set_language/pl`)
- **Set User Role**: `/set_role/<role>` (e.g., `/set_role/Admin`, `/set_role/Hr`, etc.)
- **Dashboards**:
  - Admin Dashboard: `/dashboard`
  - Inovices Dashboard: `/invoice`
  - Finance Dashboard: `/finance`
  - Projects: `/projects`

---

## How to Change User Role

To dynamically change the user role, follow these steps:

### User Menu Role Selection
1. Navigate to the **User Menu** located in the top-right corner of the dashboard.
2. Select a role from the dropdown by clicking:
   - "Set Admin"
   - "Set HR"
   - "Set Finance"
   - "Set Superadmin"
3. The role will dynamically update, and the page will refresh with the new role's dashboard and permissions.

Alternatively, directly access the URL `/set_role/<role>` replacing `<role>` with:
- `Admin`
- `Hr`
- `Finance`
- `Superadmin`

Example:
```bash
http://localhost:5000/set_role/Admin
```

---

## Directory Structure

```plaintext
ayist-group-task/
├── app/
│   ├── static/          # CSS, JavaScript, and other static files
│   ├── templates/       # HTML templates for Flask
│   ├── app.py           # Main application file
│   ├── translations/    # Localization files
│   └── requirements.txt # Python dependencies
├── .env                 # Environment variables (user-defined)
└── README.md            # Documentation (this file)
```

---

## Localization

The application supports English and Polish. To add new translations:
1. Create a directory inside `translations` for the new language code (e.g., `fr` for French).
2. Use Flask-Babel commands to extract and compile translations.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

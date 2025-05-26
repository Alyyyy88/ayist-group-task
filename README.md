# Ayist Group Dashboard

Ayist Group Dashboard is a role-based web application built using Flask. It provides a customizable user interface tailored to specific roles such as Admin, HR, Finance, and Superadmin. The application includes dynamic dashboards, employee activities, new joiner information, and other useful modules to streamline organizational workflows.

## Features

- **Role-Based Access Control**: Tailored dashboards and features for Admin, HR, Finance, and Superadmin roles.
- **Dynamic Dashboards**: Interactive dashboards showcasing real-time data like employee activities, projects, invoices, and company stats.
- **Multi-Language Support**: Built-in localization with English and Polish translations.
- **HR Dashboard**: Displays recent employee activities, new joiner onboarding progress, and HR stats.
- **Finance Dashboard**: Provides financial overviews, including income, expenses, and profit.
- **Customizable Navigation**: Dynamic menu based on user roles.
- **Project Summaries**: Track project progress, status, and client information.

## Tech Stack

This project uses the following technologies:

- **Backend**: Python (Flask)
- **Frontend**: HTML5, Jinja2, Tailwind CSS, JavaScript
- **Environment Management**: Python's `dotenv` for environment variables
- **Localization**: Flask-Babel for multi-language support
- **Icons**: Font Awesome for rich iconography

## Prerequisites

Before running this project, ensure you have the following installed:

- Python (>= 3.6)
- Flask (>= 2.0)
- Pip (Python package manager)
- A modern web browser

## Installation and Setup

Follow these steps to set up the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/ayist-group/ayist-dashboard.git
   cd ayist-dashboard
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add the following:
     ```
     FLASK_APP=app.py
     FLASK_ENV=development
     SECRET_KEY=your_secret_key
     ```

5. Run the Flask development server:
   ```bash
   flask run
   ```
   Or:
   ```bash
   python app.py
   ```

6. Access the application in your browser:
   ```
   http://localhost:5000
   ```

## Usage

- **Set Language**: Use `/set_language/<lang_code>` to switch between English (`en`) and Polish (`pl`).
- **Set User Role**: Use `/set_role/<role>` to dynamically change the role (`Admin`, `Hr`, `Finance`, `Superadmin`).
- **Navigate to Dashboards**:
  - Dashboard: `/dashboard`
  - Projects: `/projects`
  - Invoices: `/invoices`
  - HR Dashboard: `/staff`
  - Finance Dashboard: `/finance`

## Directory Structure

```
ayist-dashboard/
├── static/                # CSS, JavaScript, and other static files
│   ├── js/
│   ├── css/
├── templates/             # HTML templates for Flask
│   ├── layout.html        # Base layout
│   ├── dashboard.html     # Main dashboard template
│   ├── projects.html      # Projects module
├── translations/          # Localization files for Flask-Babel
├── app.py                 # Main Flask application file
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## Key Flask Routes

| Route                | Description                  |
|----------------------|------------------------------|
| `/`                  | Home page                   |
| `/dashboard`         | Main dashboard              |
| `/projects`          | Projects dashboard          |
| `/invoices`          | Invoices dashboard          |
| `/staff`             | HR dashboard                |
| `/finance`           | Finance dashboard           |
| `/set_language/<lang>`| Switch language (en/pl)     |
| `/set_role/<role>`   | Set user role dynamically    |

## Localization

The application supports multiple languages using Flask-Babel. To add new translations:

1. Create a new directory inside `translations` for the language code (e.g., `fr` for French).
2. Use Babel commands to extract and compile translations.

## Contributing

We welcome contributions to enhance the Ayist Group Dashboard. To contribute:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/your-feature`.
3. Commit your changes: `git commit -m "Add your feature"`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any inquiries, please contact the Ayist Group team at support@ayistgroup.com.

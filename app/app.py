from flask import Flask, render_template, request, session, redirect, url_for
from dotenv import load_dotenv
import os
from flask_babel import Babel, gettext as _

load_dotenv()

app = Flask(__name__)
app.secret_key = 'dwadawdawdawdawidwaxiaindxa'

app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = '../translations'

# Language selector function
def get_locale():
    if 'language' in session:
        return session['language']
    return 'en'


babel = Babel(app, locale_selector=get_locale)

@app.route('/set_language/<lang_code>')
def set_language(lang_code):
    if lang_code in ['en', 'pl']:
        session['language'] = lang_code
    return redirect(request.referrer or url_for('index'))

@app.route('/')
def index():
    print('Current language:', session.get('language'))
    return render_template('layout.html')


@app.route('/set_role/<role>')
def set_role(role):
    # Set the user role dynamically
    session['user_role'] = role
    return redirect(request.referrer or url_for('index'))

def get_user_role():
    return session.get('user_role')
# ROUTES FOR PAGES

@app.route('/dashboard')
def dashboard():
    dashboard_data = {
        'total_staff': 42,
        'active_projects': 7,
        'new_documents': 12,
        'profit': 24500,
        'storage_used': 4.5,
        'storage_limit': 10,
        'system_version': '1.0.0',
        'last_updated': '2025-05-24'
    }
    return render_template('dashboard.html', data=dashboard_data)


@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/invoices')
def invoices():
    return render_template('invoices.html')

@app.route('/reporting')
def reporting():
    return render_template('reporting.html')

@app.route('/staff')
def staff():
    return render_template('staff.html')

@app.route('/document')
def document():
    return render_template('document.html')

@app.route('/subplan')
def subplan():
    return render_template('subplan.html')

@app.route('/usermanagement')
def usermanagement():
    return render_template('usermanagement.html')

@app.route('/companyreg')
def companyreg():
    return render_template('companyreg.html')   

@app.route('/finance')
def finance():
    return render_template('finance.html')

@app.route('/settings')
def settings(): 
    return render_template('settings.html')

@app.route('/payroll')
def payroll():
    return render_template('payroll.html')

@app.context_processor
def utility_processor():
    def is_active(path, current):
        return "bg-indigo-100 text-blue-800  font-bold" if path == current else ""
     # Define navigation items by role
    def get_nav_items():
        # Common items for all users
        common_items = [
            {'url': '/dashboard', 'icon': 'fa-solid fa-house text-gray-500', 'label': _('Dashboard')}
        ]
        
        # Role-specific items
        role_items = {
            
            'Admin': [
                {'url': '/projects', 'icon': 'fa-solid fa-folder text-yellow-200', 'label': _('Projects')},
                {'url': '/finance', 'icon': 'fa-solid fa-sack-dollar text-green-500', 'label': _('Finance')},
                {'url': '/invoices', 'icon': 'fa-solid fa-receipt text-blue-500', 'label': _('Invoices')},
                {'url': '/reporting', 'icon': 'fa-solid fa-chart-line text-orange-300', 'label': _('Reporting')},
                {'url': '/staff', 'icon': 'fa-solid fa-users text-purple-500', 'label': _('Staff')},
                {'url': '/document', 'icon': 'fa-solid fa-file-text text-orange-300', 'label': _('Documents')},
                {'url': '/companyreg', 'icon': 'fa-solid fa-address-card text-red-400', 'label': _('Company Registration')},
                {'url': '/usermanagement', 'icon': 'fa-solid fa-user text-black', 'label': _('User Management')},
                {'url': '/subplan', 'icon': 'fa-solid fa-business-time text-orange-300', 'label': _('Subscription Plan')},
            ],
            'Hr': [
                {'url': '/staff', 'icon': 'fa-solid fa-users text-purple-500', 'label': _('Staff')},
                {'url': '/document', 'icon': 'fa-solid fa-file-text text-orange-300', 'label': _('Documents')},
                {'url': '/payroll', 'icon': 'fa-solid fa-money-bill text-green-500', 'label': _('Payroll')},

            ],
            'Finance': [
                {'url': '/finance', 'icon': 'fa-solid fa-sack-dollar text-green-500', 'label': _('Finance')},
                {'url': '/invoices', 'icon': 'fa-solid fa-receipt text-blue-500', 'label': _('Invoices')},  
                {'url': '/reporting', 'icon': 'fa-solid fa-chart-line text-orange-300', 'label': _('Reporting')},
                {'url': '/document', 'icon': 'fa-solid fa-file-text text-orange-300', 'label': _('Documents')}

            ],
            'Superadmin': [
                {'url': '/projects', 'icon': 'fa-solid fa-folder text-yellow-200', 'label': _('Projects')},
                {'url': '/staff', 'icon': 'fa-solid fa-users text-purple-500', 'label': _('Staff')},
                {'url': '/document', 'icon': 'fa-solid fa-file-text text-orange-300', 'label': _('Documents')},
                {'url': '/finance', 'icon': 'fa-solid fa-sack-dollar text-green-500', 'label': _('Finance')},
                {'url': '/invoices', 'icon': 'fa-solid fa-receipt text-blue-500', 'label': _('Invoices')},
                {'url': '/reporting', 'icon': 'fa-solid fa-chart-line text-orange-300', 'label': _('Reporting')},
                {'url': '/usermanagement', 'icon': 'fa-solid fa-user text-black', 'label': _('User Management')},
                {'url': '/subplan', 'icon': 'fa-solid fa-business-time text-orange-300', 'label': _('Subscription Plan')},
                {'url': '/companyreg', 'icon': 'fa-solid fa-address-card text-red-400', 'label': _('Company Registration')},
                {'url': '/settings', 'icon': 'fa-solid fa-gears text-gray-500', 'label': _('Settings')}

            ]
        }
        
        role = session.get('user_role')
        if not role:
            return []  # No nav if no role
        return common_items + role_items.get(role, [])

    def has_document_access():
        role = session.get('user_role')
        # All roles in your system appear to have document access based on your navigation items
        return role in ['Admin', 'Hr', 'Finance', 'Superadmin']
    
    # Add a function to check if user has specific roles
    def has_any_role(roles):
        user_role = session.get('user_role')
        return user_role in roles
    
    return dict(
        is_active=is_active, 
        get_nav_items=get_nav_items, 
        has_document_access=has_document_access,
        has_any_role=has_any_role
    ) 

if __name__ == '__main__':
    app.run(debug=True)

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

    return redirect(url_for('dashboard'))


@app.route('/set_role/<role>')
def set_role(role):
    # Set the user role dynamically
    session['user_role'] = role
    return redirect(request.referrer or url_for('index'))

def get_user_role():
    return session.get('user_role' , 'Admin')


# ROUTES FOR PAGES
@app.route('/dashboard')
def dashboard():

    hr_data = get_hr_data()
    return render_template('dashboard.html' , hr_data=hr_data,)


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

@app.route('/useractivity')
def useractivity():
    return render_template('useractivity.html')



def get_projects():
        # Return a list of dummy projects
        projects = [
            {
                'id': 1,
                'name': 'Website Redesign',
                'client': 'ABC Corporation',
                'status': _('In Progress'),
                'progress': 65
            },
            {
                'id': 2,
                'name': 'Mobile App Development',
                'client': 'TechStart Inc.',
                'status': _('Pending'),
                'progress': 30
            },
            {
                'id': 3,
                'name': 'ERP Implementation',
                'client': 'Global Logistics Ltd.',
                'status': _('Completed'),
                'progress': 100
            },
            {
                'id': 4,
                'name': 'Network Infrastructure',
                'client': 'City Hospital',
                'status': _('In Progress'),
                'progress': 45
            },
            {
                'id': 5,
                'name': 'Data Migration',
                'client': 'Financial Services Co.',
                'status': _('On Hold'),
                'progress': 20
            }
        ]
        return projects


def get_hr_data():
    hr_data = {
            'recent_employee_activities': [
                {
                    'employee_name': 'Sarah Johnson',
                    'activity': 'Checked in at 08:45 AM',
                    'time': '30m ago',
                    'icon': 'fa-clock',
                    'color': 'green'
                },

                {
                    'employee_name': 'Michael Smith',
                    'activity': 'Submitted leave request',
                    'time': '1h ago',
                    'icon': 'fa-paper-plane',
                    'color': 'blue'
                    },
              {
                    'employee_name': 'Emily Davis',
                    'activity': 'Completed training module',
                    'time': '2h ago',
                    'icon': 'fa-graduation-cap',
                    'color': 'purple'
                },
                 
            ],
            'employee_activities': [
                {
                    'employee_name': 'John Doe',
                    'activity': 'Checked in at 09:00 AM',
                    'time': '1h ago',
                    'icon': 'fa-clock',
                    'color': 'green',
                    'attendance': 'Present'
                },
                {
                    'employee_name': 'Jane Smith',
                    'activity': 'Submitted expense report',
                    'time': '2h ago',
                    'icon': 'fa-file-alt',
                    'color': 'blue',
                    'attendance': 'Present'
                },
                {
                    'employee_name': 'Alice Johnson',
                    'activity': 'Updated project status',
                    'time': '3h ago',
                    'icon': 'fa-tasks',
                    'color': 'orange',
                    'attendance': 'Present'
                },
                {
                    'employee_name': 'Bob Brown',
                    'activity': 'Checked out at 05:00 PM',
                    'time': '4h ago',
                    'icon': 'fa-sign-out-alt',
                    'color': 'red',
                    'attendance': 'Absent'
                },
                {
                    'employee_name': 'Charlie Green',
                    'activity': 'Attended team meeting',
                    'time': '5h ago',
                    'icon': 'fa-users',
                    'color': 'purple',
                    'attendance': 'Absent'

                },

            ],
            'new_joiners': [
                {
                    'name': 'David Kim',
                    'position': 'Senior UI/UX Designer',
                    'join_date': 'May 24, 2025',
                    'onboarding_progress': 75,
                    'status': 'active' 
                },
                {
                    'name': 'Laura Chen',
                    'position': 'Data Analyst',
                    'join_date': 'May 20, 2025',
                    'onboarding_progress': 50,
                    'status': 'away'

                },
                {
                    'name': 'James Brown',
                    'position': 'Project Manager',
                    'join_date': 'May 18, 2025',
                    'onboarding_progress': 100,
                    'status': 'inactive'
                },
                {
                    'name': 'Olivia Garcia',
                    'position': 'Software Engineer',
                    'join_date': 'May 15, 2025',
                    'onboarding_progress': 30,
                    'status': 'active'
                
                },
            ],
            'hr_stats': {
                'attendance_rate': 96.5,
                'leave_requests': 8,
                'open_positions': 5,
                'training_completion': 87
            }
        }
    return hr_data


@app.context_processor
def utility_processor():
    def is_active(path, current):
        if path == '/dashboard' and (current == '/dashboard' or current == '/'):
            return "bg-indigo-100 text-blue-800 font-bold"
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
                {'url': '/document', 'icon': 'fa-solid fa-file-text text-orange-500', 'label': _('Documents')},
                {'url': '/companyreg', 'icon': 'fa-solid fa-address-card text-red-400', 'label': _('Company Registration')},
                {'url': '/usermanagement', 'icon': 'fa-solid fa-user text-black', 'label': _('User Management')},
                {'url': '/subplan', 'icon': 'fa-solid fa-business-time text-orange-300', 'label': _('Subscription Plan')},
            ],
            'Hr': [
                {'url': '/staff', 'icon': 'fa-solid fa-users text-purple-500', 'label': _('Staff')},
                {'url': '/document', 'icon': 'fa-solid fa-file-text text-orange-500', 'label': _('Documents')},
                {'url': '/payroll', 'icon': 'fa-solid fa-money-bill text-green-500', 'label': _('Payroll')},
                {'url': '/useractivity', 'icon': 'fa-solid fa-user-clock text-indigo-500', 'label': _('User Activity')},

            ],
            'Finance': [
                {'url': '/finance', 'icon': 'fa-solid fa-sack-dollar text-green-500', 'label': _('Finance')},
                {'url': '/invoices', 'icon': 'fa-solid fa-receipt text-blue-500', 'label': _('Invoices')},  
                {'url': '/reporting', 'icon': 'fa-solid fa-chart-line text-orange-300', 'label': _('Reporting')},
                {'url': '/document', 'icon': 'fa-solid fa-file-text text-orange-500', 'label': _('Documents')}

            ],
            'Superadmin': [
                {'url': '/projects', 'icon': 'fa-solid fa-folder text-yellow-200', 'label': _('Projects')},
                {'url': '/staff', 'icon': 'fa-solid fa-users text-purple-500', 'label': _('Staff')},
                {'url': '/document', 'icon': 'fa-solid fa-file-text text-orange-500', 'label': _('Documents')},
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

    def has_any_role(roles):
        user_role = session.get('user_role')
        return user_role in roles
    
    return dict(
        is_active=is_active, 
        get_nav_items=get_nav_items, 
        has_any_role=has_any_role,
        get_projects=get_projects,
    ) 

if __name__ == '__main__':
    app.run(debug=True)

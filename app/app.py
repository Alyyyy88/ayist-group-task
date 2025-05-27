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
    projects_list = get_projects_page()
    
    return render_template(
        'projects.html',
        projects=projects_list,
    )

@app.route('/projects/<int:project_id>')
def project_detail(project_id):
    project = get_project_by_id(int(project_id))
    if project is None:
        return redirect(url_for('projects'))  
    return render_template(
        'project_detail.html',
        project=project,
    )

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
    hr_data = get_hr_data()
    return render_template('useractivity.html', hr_data=hr_data)


def get_projects_page():
   projects = [
        {
            "id": 1,
            "name": "Website Redesign",
            "description": "Complete overhaul of corporate website with new design and features",
            "client": "ABC Corporation",
            "status": _("In Progress"),
            "progress": 65,
            "total_tasks": 48,
            "completed_tasks": 31,
            "due_date": "15 Jun, 2025",
            "budget_spent": "$12,500",
            "budget_total": "$25,000",
            "team_members": [
                {"id": 101, "name": "John Doe", "avatar": "user1.jpg"},
                {"id": 102, "name": "Jane Smith", "avatar": "user2.jpg"},
                {"id": 103, "name": "Robert Johnson", "avatar": "user3.jpg"}
            ],
            "files": [
                {"name": "Website Mockup.pdf", "size": "4.2 MB", "uploaded": "Yesterday", "author": "Jane Smith"},
                {"name": "Requirements Doc.docx", "size": "1.8 MB", "uploaded": "3 days ago", "author": "John Doe"},
                {"name": "Color Palette.png", "size": "0.8 MB", "uploaded": "1 week ago", "author": "Robert Johnson"}
            ],
            "activities": [
                {"user": "Jane Smith", "action": "Updated homepage design", "time": "Today", "avatar": "user2.jpg"},
                {"user": "John Doe", "action": "Added contact form functionality", "time": "Yesterday", "avatar": "user1.jpg"},
                {"user": "Robert Johnson", "action": "Fixed responsive layout issues", "time": "2 days ago", "avatar": "user3.jpg"}
            ],
            "spendings": [
                {"manager": "Jane Smith", "date": "May 20, 2025", "amount": "$3,200", "status": "Approved"},
                {"manager": "John Doe", "date": "May 15, 2025", "amount": "$4,800", "status": "Complete"},
                {"manager": "Robert Johnson", "date": "May 10, 2025", "amount": "$2,500", "status": "Pending"}
            ]
        },
        {
            "id": 2,
            "name": "Mobile App Development",
            "description": "Creation of native mobile application for iOS and Android platforms",
            "client": "TechStart Inc.",
            "status": _("Pending"),
            "progress": 30,
            "total_tasks": 36,
            "completed_tasks": 10,
            "due_date": "30 Jul, 2025",
            "budget_spent": "$8,500",
            "budget_total": "$35,000",
            "team_members": [
                {"id": 104, "name": "Alice Brown", "avatar": "user4.jpg"},
                {"id": 105, "name": "Michael Chen", "avatar": "user5.jpg"}
            ],
            "files": [
                {"name": "App Wireframes.pdf", "size": "3.1 MB", "uploaded": "Yesterday", "author": "Alice Brown"},
                {"name": "API Documentation.pdf", "size": "2.5 MB", "uploaded": "2 days ago", "author": "Michael Chen"}
            ],
            "activities": [
                {"user": "Alice Brown", "action": "Created initial wireframes", "time": "Yesterday", "avatar": "user4.jpg"},
                {"user": "Michael Chen", "action": "Set up development environment", "time": "3 days ago", "avatar": "user5.jpg"}
            ],
            "spendings": [
                {"manager": "Alice Brown", "date": "May 22, 2025", "amount": "$5,000", "status": "Approved"},
                {"manager": "Michael Chen", "date": "May 18, 2025", "amount": "$3,500", "status": "Pending"}
            ]
        },
        {
            "id": 3,
            "name": "ERP Implementation",
            "description": "Enterprise resource planning system implementation and migration",
            "client": "Global Logistics Ltd.",
            "status": _("Completed"),
            "progress": 100,
            "total_tasks": 64,
            "completed_tasks": 64,
            "due_date": "10 Apr, 2025",
            "budget_spent": "$58,000",
            "budget_total": "$60,000",
            "team_members": [
                {"id": 106, "name": "Sarah Johnson", "avatar": "user6.jpg"},
                {"id": 107, "name": "David Kim", "avatar": "user7.jpg"},
                {"id": 108, "name": "Emily Davis", "avatar": "user8.jpg"},
                {"id": 109, "name": "James Wilson", "avatar": "user9.jpg"}
            ],
            "files": [
                {"name": "Final Report.pdf", "size": "5.8 MB", "uploaded": "Apr 10, 2025", "author": "Sarah Johnson"},
                {"name": "System Manual.pdf", "size": "12.3 MB", "uploaded": "Apr 9, 2025", "author": "David Kim"},
                {"name": "Training Materials.zip", "size": "45.6 MB", "uploaded": "Apr 5, 2025", "author": "Emily Davis"}
            ],
            "activities": [
                {"user": "Sarah Johnson", "action": "Submitted final project report", "time": "Apr 10, 2025", "avatar": "user6.jpg"},
                {"user": "David Kim", "action": "Completed user training", "time": "Apr 8, 2025", "avatar": "user7.jpg"},
                {"user": "Emily Davis", "action": "Finalized data migration", "time": "Apr 5, 2025", "avatar": "user8.jpg"}
            ],
            "spendings": [
                {"manager": "Sarah Johnson", "date": "Apr 8, 2025", "amount": "$15,000", "status": "Complete"},
                {"manager": "David Kim", "date": "Apr 2, 2025", "amount": "$23,000", "status": "Complete"},
                {"manager": "Emily Davis", "date": "Mar 25, 2025", "amount": "$20,000", "status": "Complete"}
            ]
        },
        {
            "id": 4,
            "name": "Network Infrastructure",
            "description": "Upgrade and expansion of corporate network infrastructure",
            "client": "City Hospital",
            "status": _("In Progress"),
            "progress": 45,
            "total_tasks": 42,
            "completed_tasks": 19,
            "due_date": "20 Jun, 2025",
            "budget_spent": "$32,000",
            "budget_total": "$75,000",
            "team_members": [
                {"id": 110, "name": "Thomas Brown", "avatar": "user10.jpg"},
                {"id": 111, "name": "Laura Martinez", "avatar": "user11.jpg"},
                {"id": 112, "name": "Kevin Lee", "avatar": "user12.jpg"}
            ],
            "files": [
                {"name": "Network Diagram.pdf", "size": "3.4 MB", "uploaded": "Last week", "author": "Thomas Brown"},
                {"name": "Equipment List.xlsx", "size": "1.2 MB", "uploaded": "2 weeks ago", "author": "Laura Martinez"},
                {"name": "Implementation Plan.docx", "size": "2.8 MB", "uploaded": "3 weeks ago", "author": "Kevin Lee"}
            ],
            "activities": [
                {"user": "Thomas Brown", "action": "Installed core switches", "time": "Yesterday", "avatar": "user10.jpg"},
                {"user": "Laura Martinez", "action": "Configured VLAN routing", "time": "3 days ago", "avatar": "user11.jpg"},
                {"user": "Kevin Lee", "action": "Completed cable installation in Wing A", "time": "1 week ago", "avatar": "user12.jpg"}
            ],
            "spendings": [
                {"manager": "Thomas Brown", "date": "May 15, 2025", "amount": "$18,000", "status": "Approved"},
                {"manager": "Laura Martinez", "date": "May 5, 2025", "amount": "$14,000", "status": "Complete"},
                {"manager": "Kevin Lee", "date": "Apr 28, 2025", "amount": "$0", "status": "Pending"}
            ]
        },
        {
            "id": 5,
            "name": "Data Migration",
            "description": "Legacy system data migration to new cloud-based platform",
            "client": "Financial Services Co.",
            "status": _("On Hold"),
            "progress": 20,
            "total_tasks": 28,
            "completed_tasks": 5,
            "due_date": "15 Aug, 2025",
            "budget_spent": "$7,800",
            "budget_total": "$45,000",
            "team_members": [
                {"id": 113, "name": "Mark Taylor", "avatar": "user13.jpg"},
                {"id": 114, "name": "Sophia Rodriguez", "avatar": "user14.jpg"}
            ],
            "files": [
                {"name": "Data Mapping Doc.xlsx", "size": "3.7 MB", "uploaded": "2 weeks ago", "author": "Mark Taylor"},
                {"name": "Migration Plan.pdf", "size": "2.1 MB", "uploaded": "3 weeks ago", "author": "Sophia Rodriguez"}
            ],
            "activities": [
                {"user": "Mark Taylor", "action": "Project put on hold pending security review", "time": "Yesterday", "avatar": "user13.jpg"},
                {"user": "Sophia Rodriguez", "action": "Completed initial data analysis", "time": "2 weeks ago", "avatar": "user14.jpg"}
            ],
            "spendings": [
                {"manager": "Mark Taylor", "date": "May 10, 2025", "amount": "$4,500", "status": "Complete"},
                {"manager": "Sophia Rodriguez", "date": "May 5, 2025", "amount": "$3,300", "status": "Complete"}
            ]
        },
        {
            "id": 6,
            "name": "SnowUI",
            "description": "User interface redesign for winter collection",
            "client": "Frost Industries",
            "status": "In Progress",
            "progress": 51,
            "total_tasks": 48,
            "completed_tasks": 15,
            "due_date": "29 Jan, 2025",
            "budget_spent": "$15,000",
            "budget_total": "$30,000",
            "team_members": [
                {"id": 101, "name": "Karina Clark", "avatar": "user15.jpg"},
                {"id": 102, "name": "Marcus Blake", "avatar": "user16.jpg"},
                {"id": 103, "name": "Terry Barry", "avatar": "user17.jpg"}
            ],
            "files": [
                {"name": "Project tech requirements.pdf", "size": "5.8 MB", "uploaded": "Just now", "author": "Karina Clark"},
                {"name": "Dashboard-design.jpg", "size": "2.3 MB", "uploaded": "59 minutes ago", "author": "Marcus Blake"},
                {"name": "Completed Project Stylings.pdf", "size": "2.9 MB", "uploaded": "12 hours ago", "author": "Terry Barry"},
                {"name": "Create Project Wireframes.xls", "size": "1.2 MB", "uploaded": "Today, 11:59 AM", "author": "Roth Bloom"}
            ],
            "activities": [
                {"user": "Karina Clark", "action": "You have a bug that needs to be fixed.", "time": "Just now", "avatar": "user15.jpg"},
                {"user": "Marcus Blake", "action": "Released a new version", "time": "59 minutes ago", "avatar": "user16.jpg"},
                {"user": "Roth Bloom", "action": "Submitted a bug", "time": "12 hours ago", "avatar": "user18.jpg"},
                {"user": "Natali Craig", "action": "Modified A data in Page X", "time": "Today, 11:59 AM", "avatar": "user19.jpg"},
                {"user": "Drew Cano", "action": "Deleted a page in Project X", "time": "Feb 2, 2025", "avatar": "user20.jpg"}
            ],
            "spendings": [
                {"manager": "ByeWind", "date": "Jun 24, 2025", "amount": "$942.00", "status": "In Progress"},
                {"manager": "Natali Craig", "date": "Mar 10, 2025", "amount": "$881.00", "status": "Complete"},
                {"manager": "Drew Cano", "date": "Nov 10, 2025", "amount": "$409.00", "status": "Pending"},
                {"manager": "Orlando Diggs", "date": "Dec 20, 2025", "amount": "$953.00", "status": "Approved"},
                {"manager": "Andi Lane", "date": "Jul 25, 2025", "amount": "$907.00", "status": "Rejected"}
            ]
        }
    ]
   return projects

def get_project_by_id(project_id):
    projects = get_projects_page()
    for project in projects:
        if project["id"] == project_id:
            return project
    return None




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
                    'employee_name': _('Sarah Johnson'),
                    'activity': _('Checked in at 08:45 AM'),
                    'time': _('30m ago'),
                    'icon': 'fa-clock',
                    'color': 'green'
                },

                {
                    'employee_name': _('Michael Smith'),
                    'activity': _('Submitted leave request'),
                    'time': _('1h ago'),
                    'icon': 'fa-paper-plane',
                    'color': 'blue'
                },
                {
                    'employee_name': _('Emily Davis'),
                    'activity': _('Completed training module'),
                    'time': _('2h ago'),
                    'icon': 'fa-graduation-cap',
                    'color': 'purple'
                },
                 
            ],
            'employee_activities': [
                {
                    'employee_name': _('John Doe'),
                    'activity': _('Checked in at 09:00 AM'),
                    'time': _('1h ago'),
                    'icon': 'fa-clock',
                    'color': 'green',
                    'attendance': 'Present',
                    'type': 'check-in'
                },
                {
                    'employee_name': _('Jane Smith'),
                    'activity': _('Submitted expense report'),
                    'time': _('2h ago'),
                    'icon': 'fa-file-alt',
                    'color': 'blue',
                    'attendance': 'Present',
                    'type': 'expense'
                },
                {
                    'employee_name': _('Alice Johnson'),
                    'activity': _('Updated project status'),
                    'time': _('3h ago'),
                    'icon': 'fa-tasks',
                    'color': 'orange',
                    'attendance': 'Present',
                    'type': 'update'
                },
                {
                    'employee_name': _('Bob Brown'),
                    'activity': _('Checked out at 05:00 PM'),
                    'time': _('4h ago'),
                    'icon': 'fa-sign-out-alt',
                    'color': 'red',
                    'attendance': 'Absent',
                    'type': 'check-out'
                },
                {
                    'employee_name': _('Charlie Green'),
                    'activity': _('Attended team meeting'),
                    'time': _('5h ago'),
                    'icon': 'fa-users',
                    'color': 'purple',
                    'attendance': 'Absent',
                    'type': 'meeting'
                },
                {
                    'employee_name': _('David Kim'),
                    'activity': _('Checked out at 05:30 AM'),
                    'time': _('6h ago'),
                    'icon': 'fa-sign-out-alt',
                    'color': 'red',
                    'attendance': 'On Leave',
                    'type': 'Check-out'
                }

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
            'performance_evaluations': [
                {
                    'title': _('Quarterly Performance Review'),
                    'date': '2025-05-15',
                    'comment': _('John Doe has shown excellent performance in the last quarter, exceeding expectations in project delivery and team collaboration.'),
                    'rating': 4,
        
                },
                {
                    'title': _('Mid-Year Evaluation'),
                    'date': '2025-06-01',
                    'comment': _('Jane Smith has made significant contributions to the team, particularly in improving client relationships and project management.'),
                    'rating': 4,
                },
                {
                    'title': _('Annual Performance Appraisal'),
                    'date': '2025-12-20',
                    'comment': _('Alice Johnson has consistently performed at a high level, demonstrating leadership and innovation in her role.'),
                    'rating': 3,
                },
                {
                    'title': _('Project Completion Review'),
                    'date': '2025-07-10',
                    'comment': _('Bob Brown successfully led the project team to complete the XYZ project ahead of schedule, showcasing excellent project management skills.'),
                    'rating': 2,
                }    

            ],
            'documents': [
                {
                    'title': _('Employee Handbook'),
                    'type': 'PDF',
                    'uptated_date': '2025-05-01',
                    'description': _('The employee handbook outlines company policies, procedures, and benefits for all employees.'),
                },{
                    'title': _('Code of Conduct'),
                    'type': 'PDF',
                    'uptated_date': '2025-04-15',
                    'description': _('The code of conduct sets the standards for professional behavior and ethics expected from all employees.'),
                },
                {
                    'title': _('Health and Safety Guidelines'),
                    'type': 'PDF',
                    'uptated_date': '2025-03-10',
                    'description': _('These guidelines provide essential information on workplace safety and health protocols.'),

                },
                {
                    'title': _('Performance Evaluation Form'),
                    'type': 'DOCX',
                    'uptated_date': '2025-02-20',
                    'description': _('The performance evaluation form is used to assess employee performance and set goals for the upcoming period.'),
                }

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

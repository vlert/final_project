import database

# Function Definitions
def initializing():
    db = database.Database()
    db.add_table('login', database.Table('/mnt/data/login.csv'))
    db.add_table('persons', database.Table('/mnt/data/persons.csv'))
    db.add_table('projects', database.Table('projects.csv'))  # Assuming this file exists
    db.add_table('invitations', database.Table('invitations.csv'))  # Assuming this file exists
    db.add_table('supervision_requests', database.Table('supervision_requests.csv'))  # Assuming this file exists
    return db

def login():
    db = initializing()
    username = input("Enter username: ")
    password = input("Enter password: ")
    login_table = db.get_table('login')
    for user in login_table.data:
        if user['username'] == username and user['password'] == password:
            return [user['id'], user['role']]
    return None

def exit(db):
    db.save_all()

# User and Role Class Definitions
class User:
    def __init__(self, user_id, db):
        self.user_id = user_id
        self.db = db

class Student(User):
    def create_project(self, project_info):
        print("Creating project...")
        # Implement project creation logic

    def view_invitations(self):
        print("Viewing invitations...")
        # Implement logic to view invitations

    def accept_invitation(self, invitation_id):
        print(f"Accepting invitation {invitation_id}...")
        # Implement logic to accept invitation

class LeadStudent(Student):
    def modify_project_info(self, project_id, new_info):
        print(f"Modifying project {project_id} info...")
        # Implement logic to modify project info

class Faculty(User):
    def view_supervision_requests(self):
        print("Viewing supervision requests...")
        # Implement logic to view supervision requests

    def respond_to_supervision_request(self, request_id, response):
        print(f"Responding to supervision request {request_id}...")
        # Implement logic to respond to supervision request

class AdvisingFaculty(Faculty):
    def evaluate_project(self, project_id, evaluation_criteria):
        print(f"Evaluating project {project_id}...")
        # Implement logic to evaluate project

class Admin(User):
    def update_table(self, table_name, data):
        print(f"Updating table {table_name}...")
        # Implement logic to update a table


# Main Program Execution
val = login()

if val:
    user_id, role = val
    db = initializing()
    if role == 'Admin':
        admin = Admin(user_id, db)
        admin.update_table("projects", {"new": "data"})
    elif role == 'Student':
        student = Student(user_id, db)
        student.create_project({"name": "New Project"})
    elif role == 'Lead':
        lead = LeadStudent(user_id, db)
        lead.modify_project_info("proj1", {"new_info": "updated info"})
    elif role == 'Faculty':
        faculty = Faculty(user_id, db)
        faculty.view_supervision_requests()
    elif role == 'Advisor':
        advisor = AdvisingFaculty(user_id, db)
        advisor.evaluate_project("proj2", "Excellent")
else:
    print("Login failed.")

db = initializing()
exit(db)

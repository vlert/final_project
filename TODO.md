
# TODO List for Final Project

## Database Initialization
[ ] Generalize the CSV file reading functionality:
    - Modify the existing CSV reading code to handle any CSV file.
    - Ensure dynamic reading of different CSV files and storing data in a list of dictionaries.
- [ ] Develop a `Database` class:
    - Implement the class to manage multiple tables (represented by CSV files).
    - Include methods to add new tables and retrieve existing tables.
- [ ] Create a `Table` class:
    - Design the class to encapsulate data handling for a single CSV file.
    - Implement methods for reading CSV data, adding new rows (insert operation), and updating existing rows (update operation).
    - Include functionality to save modified data back to the CSV file.


## User Role Functions
### Student
- [ ] Implement functionality for students to view pending requests to join projects.
- [ ] Enable students to accept or deny these requests, updating the 'Member_pending_request' and 'Project' tables.
- [ ] Allow students to create a new project, becoming the lead, and update 'Project' and 'Login' tables.
- [ ] Add feature for students to send out requests for more members if needed.

### Lead
- [ ] Enable leads to see the status of their projects (pending member, pending advisor, etc.).
- [ ] Allow leads to modify project information in the 'Project' table.
- [ ] Implement functionality for leads to send requests to potential members and advisors, updating 'Member_pending_request' and 'Advisor_pending_request' tables.

### Member
- [ ] Allow members to view their project status and details.
- [ ] Enable members to modify their project information in the 'Project' table.
- [ ] Add feature for members to see who has responded to their project requests.

### Faculty
- [ ] Implement viewing functionality for faculty to see requests for becoming supervisors.
- [ ] Enable faculty to respond to these requests and evaluate projects (details in Proposal.md).

### Advisor
- [ ] Allow advisors to see and respond to supervision requests.
- [ ] Enable advisors to evaluate and approve projects (details in Proposal.md).

### Admin
- [ ] Develop admin functionalities to manage and update all database tables.

## Authentication
- [ ] Create a login system for user authentication using the 'Login' table.

## Project Management
- [ ] Implement features for creating, updating, and managing projects.
- [ ] Manage invitations and responses for project members and advisors.

## Additional Evaluation Step
- [ ] Outline the evaluation process involving advisors and faculty in Proposal.md.

### Code Structure for Database Initialization and User Role Functionalities

#### User Role Functionalities
```python
class Student:
    def view_invitations(self):
        # Code to view invitations

    def accept_invitation(self, invitation_id):
        # Code to accept an invitation

    def modify_project_details(self, project_id, new_details):
        # Code to modify project details

class LeadStudent(Student):
    def create_project(self, project_details):
        # Code to create a project

    def find_and_invite_members(self, member_ids):
        # Code to invite members

    def submit_final_report(self, report):
        # Code to submit the final project report
```

##### Admin Role
```python
class Admin:
    def manage_database(self):
        # Code for managing the overall database

    def update_table(self, table_name, data):
        # Code to update specific tables in the database
```

##### Member Student Role
```python
class MemberStudent(Student):
    def view_project_details(self, project_id):
        # Code for a member student to view their project details

    def edit_project_details(self, project_id, new_details):
        # Code for a member student to edit their project details
```

##### Faculty Role (Non-Advisor)
```python
class Faculty:
    def view_supervision_requests(self):
        # Code for faculty to view requests for supervision

    def respond_to_supervision_request(self, request_id, response):
        # Code for faculty to respond to supervision requests
```

##### Advising Faculty Role
```python
class AdvisingFaculty(Faculty):
    def approve_project(self, project_id):
        # Code for an advising faculty to approve a project

    def evaluate_project(self, project_id, evaluation_criteria):
        # Code for an advising faculty to evaluate a project
```

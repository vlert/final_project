
# TODO List for Final Project

## Database Initialization
- [ ] Initialize 'Person' table with attributes: ID, First, Last, Type.
- [ ] Initialize 'Login' table with attributes: ID, Username, Password, Role.
- [ ] Initialize 'Project' table with attributes: ProjectID, Title, Lead, Member1, Member2, Advisor, Status.
- [ ] Initialize 'Advisor_pending_request' table with attributes: ProjectID, To-be Advisor ID, Response.
- [ ] Initialize 'Member_pending_request' table with attributes: ProjectID, To-be Member ID, Response.

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

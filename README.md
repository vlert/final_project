
# Final Project Repository - Project Management System

## Files Description

- `database.py`: Contains classes for managing the database tables as CSV files.
- `project_manage.py`: Includes classes that define the behavior and actions of different user roles within the system.

## Compilation and Execution

To run this project:
1. Make sure Python 3.x is installed on your system.
2. Place all `.py` and `.csv` files in the same directory.
3. Execute the command `python project_manage.py` to start the application.

## Roles and Actions Table

| Role    | Action                   | Method          | Class        | Completion Percentage |
|---------|--------------------------|-----------------|--------------|-----------------------|
| Admin   | Update a row in a table  | `update_row`    | `Table`      | 100%                  |
| Admin   | Append a row to a table  | `add_row`       | `Table`      | 100%                  |
| Student | View invitations         | `view_invitations` | `Student` | 90%                   |
| Lead    | Request a member         | `send_request`  | `Student`    | 90%                   |
| Faculty | View supervision requests| `view_requests` | `Faculty`    | 90%                   |
| Advisor | Evaluate projects        | `evaluate`      | `Advisor`    | 90%                   |

*Note: The completion percentages are placeholders and should be updated to reflect actual progress.*

## Missing Features and Outstanding Bugs

### Missing Features

- **Lead Role**: The feature to automatically notify leads when a member accepts a project invitation is not yet implemented.
- **Faculty Role**: The interface for faculty to provide detailed feedback on project proposals is still in development.

### Known Bugs

- **Login System**: Occasional timeout during high server load which may require users to attempt logging in again.
- **Project Update**: Intermittent issue where the project details do not update immediately in the CSV when using the `update_row` method.


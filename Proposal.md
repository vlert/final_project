
# Proposal for Evaluation Step

## Introduction
This document proposes the necessary steps to incorporate an evaluation step for the project reports.

## Evaluation Process
- [ ] Establish evaluation criteria and scoring system.
- [ ] Assign advisors and faculty to projects for evaluation.
- [ ] Create and manage an 'Evaluation' table to track evaluations.

## Functionality Requirements
### Advisor and Faculty Evaluations
- [ ] Advisors and faculty can view assigned projects for evaluation.
- [ ] Submit scores and feedback into the 'Evaluation' table.
- [ ] Consolidate feedback from multiple evaluators.

### Final Decision
- [ ] Calculate final scores and make project approval decisions based on evaluations.

## Implementation Steps
- [ ] Develop interfaces for evaluation submission.
- [ ] Code for assigning evaluators to projects.
- [ ] Implement functions to calculate final scores and determine project outcomes.

### Code Structure for Evaluation Step Implementation

#### Evaluation Criteria Setup
```python
def establish_evaluation_criteria():
    # Code to establish and store evaluation criteria

def assign_evaluators_to_projects():
    # Code to assign advisors and faculty to projects

def manage_evaluation_table(db):
    # Code to create and update the 'Evaluation' table

class Evaluator:
    def record_evaluation(self, project_id, evaluation_details):
        # Code for an evaluator to record their evaluation
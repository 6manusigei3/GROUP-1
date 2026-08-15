Northstar Retail Co. — Team Charter

Project: Support Deflection MVP
Client: Northstar Retail Co.
Sprint: 5-Day Industry Working Simulation
Charter Version: 1.0
Date: 14 August 2026

1. Team Purpose

Our team will operate as a small industry delivery pod for Northstar Retail Co. The purpose of this charter is to establish how we communicate, plan, execute, review, and deliver work during the five-day Support Deflection MVP sprint.

The team will focus on delivering a practical, demonstrable MVP rather than a production-ready system. The MVP must reduce manual handling for at least two of Northstar's three repetitive support categories:

Order status
Returns and refunds
Stock availability

The team will prioritize a reliable, testable MVP and a transparent record of how the work was completed.

2. Team Goals

By the end of the sprint, the team will:

 Deliver a working prototype covering at least two ticket categories.
 Demonstrate the prototype end-to-end.
 Produce a one-page go-live readiness note.
 Maintain a transparent and traceable collaborative audit trail.
 Ensure every team member makes meaningful and visible contributions.
 Keep project work small, clearly owned, and objectively verifiable.
 Communicate blockers early and resolve issues before they threaten delivery.
 Prioritize the agreed MVP scope over unnecessary features.
3. Team Roles and Ownership

Each project-board task will have one accountable owner. Other team members may collaborate, review, or support the owner, but accountability remains with the assigned owner.

Role	Primary Responsibility
Project / Delivery Lead	Sprint coordination, board hygiene, blockers, scope, and delivery
Backend / Integration Lead	APIs, data handling, business logic, and integrations
Frontend / UX Lead	Customer interface, user flows, and usability
AI / Automation Lead	Deflection logic, prompts, decision flows, or automation
QA / Documentation Lead	Testing, acceptance checks, audit evidence, and handover documentation

Roles may overlap depending on the final team size and technical approach. No role gives a member unilateral control over project decisions.

4. Communication Agreement
Primary Channels

Primary team channel: [INSERT SLACK / TEAMS / DISCORD CHANNEL]

The project board is the single source of truth for task status.

GitHub is the source of truth for:

Code
Branches
Commits
Pull requests
Reviews
Version history
Communication Rules
Direct project questions should be acknowledged within 2 hours during agreed working hours where reasonably possible.
A blocker that prevents progress for more than 30 minutes should be communicated rather than silently worked around.
Important project decisions should not remain only in private messages.
Decisions affecting scope, architecture, deadlines, or responsibilities should be recorded in the relevant project channel or task.
Team members should communicate:
What they completed.
What they are currently working on.
What they plan to do next.
Any blockers or dependencies.
Communication should remain professional, concise, and respectful.
5. Project Board Working Agreement

The project board will make ownership, progress, and delivery status visible throughout the sprint.

Every task must have:

A clear title and description.
One accountable owner.
A priority.
A checkable Definition of Done.
An appropriate tag/category.
A relevant branch, pull request, commit, or artifact linked where applicable.
Board Workflow
BACKLOG
   ↓
READY
   ↓
IN PROGRESS
   ↓
REVIEW
   ↓
DONE
Board Status Rule

Board status must be updated on the same day that work happens.

Batched end-of-week updates are not acceptable because they weaken the audit trail.

A task may only move to DONE when its Definition of Done has been satisfied.

6. Anti-Black-Box Rule

No project-board task may represent a large, vague, or hidden body of work.

Maximum Task Size

Maximum estimated work for a single task: 4 hours.

If a task is likely to take more than four hours, it must be split into smaller tasks.

Each resulting task must produce a specific output that can be independently checked.

Example — Not Acceptable
Build the chatbot

This task is too broad and does not provide enough visibility into the work.

Example — Acceptable Breakdown
Define order-status conversation flow
Implement order-status lookup
Connect order-status lookup to customer interface
Test order-status happy path
Test missing-order scenario

Each task has a specific and verifiable outcome.

7. Definition of Done

A task is considered complete only when:

 The agreed task output exists.
 The output satisfies its Definition of Done.
 Required testing or checks have been completed.
 Relevant code or documentation has been committed or saved.
 The project board has been updated.
 The work can be traced to the relevant commit, pull request, or artifact.

A task must not be marked DONE simply because work has started or is nearly complete.

8. Git Commit and Edit Convention

Meaningful code contributions should follow this format:

<type>: <what changed> - <why it matters>
Examples
feat: add order lookup - enables shipment status responses


fix: handle missing order ID - prevents failed customer requests


test: add refund scenarios - verifies return-flow behaviour


docs: add deployment instructions - enables Northstar handover
Not Acceptable
wip
updates
changes
stuff
final
more fixes

Commit messages should clearly communicate what changed and why it matters.

9. Branch and Contribution Convention

Recommended branch format:

<type>/<task-id>-<short-description>
Examples
feature/NS-07-order-lookup


feature/NS-08-order-status-flow


fix/NS-12-invalid-input


docs/NS-17-go-live-note

Where practical, completed work should be traceable as:

Board Task
    ↓
Branch / Pull Request
    ↓
Commit / Edit
    ↓
Delivered Artifact
10. Pull Request and Review Rules

Where pull requests are used:

Significant implementation work should receive at least one peer review before merging.
Reviewers should check functionality.
Reviewers should check the Definition of Done.
Reviewers should identify obvious regressions.
The task owner is responsible for addressing review feedback.
Reviews should happen promptly so they do not become a final-day bottleneck.
Small documentation or configuration changes may be merged directly where the team agrees this is appropriate.
11. Five-Day Sprint Discipline
Day 1 — Setup

The team will:

Complete the solo baseline diagnostic.
Agree on the Team Charter.
Configure the project board.
Create at least 10 granular tasks.
Assign owners.
Assign priorities.
Define a Definition of Done for every task.
Agree on the MVP scope.

Deliverables:

Team Charter
Project Board
Assignment 1
Baseline diagnostic
Days 2–3 — Build

The team will:

Execute against the project board.
Follow branch naming conventions.
Follow commit/edit conventions.
Keep task ownership visible.
Update board status on the same day.
Raise blockers immediately.
Review work where required.
Maintain task-to-commit traceability.

Deliverable:

Working MVP implementation.

Day 4 — Checkpoint

The team will review:

Project-board activity.
Commit/edit history.
Contribution balance.
Task-to-commit traceability.
Outstanding blockers.
MVP completion status.

Any contribution or activity issues will be addressed immediately rather than waiting until the final deadline.

Deliverable:

Mid-sprint audit snapshot.

Day 5 — Delivery

The team will:

Complete the MVP.
Run final validation.
Prepare the final demonstration.
Produce the one-page go-live readiness note.
Collect the raw audit log.
Confirm task-to-commit traceability.
Complete final documentation.
Complete the confidential Peer Reliability Index.
Complete the final self-assessment.

Deliverables:

Support Deflection MVP
Go-Live Readiness Note
Audit Log
Final project artifacts
12. Conflict Resolution

We will use a three-step escalation process.

Step 1 — Discuss

The people directly involved will discuss the issue and attempt to reach a solution using:

Client requirements
Technical evidence
Project scope
Available time
Delivery risk
Step 2 — Team Decision

If the issue cannot be resolved within 30 minutes, it will be brought to the full team.

Step 3 — Delivery Lead Decision

If the team cannot reach agreement, the Project/Delivery Lead will make a temporary delivery decision so that work can continue.

The decision should be documented in the relevant project-board task or project channel.

Behaviour Standard

Disagreements should focus on:

Ideas
Requirements
Technical decisions
Implementation approaches

They should never become personal.

The following behaviours are not acceptable:

Personal attacks
Blame
Deliberately withholding information
Silent withdrawal
Sabotaging another member's work
13. Blocker Escalation

When reporting a blocker, use:

Problem
↓
Impact
↓
What has been attempted
↓
Help required
Example
Problem:
The order API is returning incomplete shipment information.


Impact:
This blocks the order-status customer flow.


Attempted:
Checked the API response and mapping logic.


Help required:
Need another team member to review the API response with me.

Team members should not remain blocked silently.

14. Zero-Activity Rule

If a team member has zero visible project activity for two consecutive days, the escalation process begins immediately.

The team will first determine whether the cause is:

A blocker.
An unclear task.
A dependency.
Workload imbalance.
Communication issue.

The team will then provide support, split work, reassign tasks, or otherwise correct the problem.

We will not wait until the final deadline to address inactivity.

15. Contribution Balance

We do not expect every team member to produce exactly the same number of commits.

Meaningful contributions may include:

Code
Testing
UX/design
Research
Documentation
Architecture
Integration
Debugging
Code review
Deployment/setup

However, every team member must have visible and meaningful contributions.

The project board and repository history should make these contributions traceable.

16. Scope Control

Because this is a one-week MVP, the team will prioritize delivery over unnecessary features.

Priority Levels

P0 — Required

Essential for the MVP and must be completed.

P1 — Important

Improves usability, reliability, or demonstration quality.

P2 — Nice to Have

Only completed if P0 and P1 work is secure.

If a new idea threatens the core MVP timeline, it should be moved to P2 rather than delaying the main deliverable.

17. Quality Standard

Before demonstrating a feature, the team should test:

 Normal/happy-path behaviour.
 Missing information.
 Invalid information.
 Expected edge cases.
 Failure/error handling.
 User-facing response quality.

Known limitations must be documented honestly in the go-live readiness note.

The team will not hide known problems simply to make the MVP appear more complete.

18. Audit Trail and Collaboration Integrity

The repository and project board must demonstrate genuine collaboration.

The audit trail should include:

Board task creation timestamps.
Board status timestamps.
Task ownership.
Branch history.
Commit history.
Pull requests.
Reviews.
Documentation changes.
Task-to-commit relationships.
Final artifact history.
Integrity Rule

The team will not:

Fabricate commits.
Backdate work.
Falsely attribute work.
Create meaningless activity.
Manipulate the audit trail.

The repository history should accurately represent how the team worked.

19. Peer Reliability Index

The Peer Reliability Index is confidential.

Individual responses:

Will not be shared verbatim between teammates.
Will not be used for public criticism.
Should be based on observed behaviour during the sprint.

Only aggregate patterns or relevant findings may be released.

20. Decision-Making Principle

When deciding whether to implement something, ask:

Does this satisfy a client MVP requirement?
Can we deliver it within the remaining time?
Can we test it?
Is ownership clear?
Can another team member understand or continue the work?
Does it introduce unnecessary risk?

If several answers are No, simplify the solution.

21. Team Commitment

By signing this charter, each team member agrees to:

Communicate proactively.
Keep work visible.
Respect agreed deadlines.
Keep board status current.
Follow the commit/edit convention.
Ask for help when blocked.
Give constructive feedback.
Respect other members' contributions.
Take responsibility for assigned work.
Help the team recover when work falls behind.
Protect the integrity of the audit trail.
Prioritize delivery of the agreed MVP over unnecessary scope.
22. Team Sign-Off

By signing below, team members confirm that they have read, discussed, and agreed to this working agreement.

Team Member	    Role	-- Signature	--Date
1. Fidel Katee  member  Fkatee,      14/8/2026
2. Emmanuel Sigei member  Esigei     14/8/2026
3. Trizah  Biwott member   Tbiwott    14/8/2026


Charter Status: Agreed and signed before build work begins.

Team Principle

Keep the work small. Keep ownership clear. Keep the board current. Make every contribution traceable.

Implement Hiring Signal Foundation.



Goal:

Add recruitment signal intelligence to improve role matching accuracy.



Important:

\- Do not add new pages.

\- Do not duplicate existing services.

\- Reuse current Role Intelligence and Alignment Report.

\- Do not modify completed workflows.



Current completed features:

\- Resume Intelligence

\- Role Intelligence

\- Alignment Report

\- Resume Optimization



Tasks:



\## Data



Add local hiring signal dataset.



Create:

data/seeds/hiring\_signals.json



Each signal should contain:

\- role

\- signal name

\- importance

\- evidence examples

\- source type

\- confidence





\## Backend



Add hiring signal service.



Integrate with existing role analysis.



Role Intelligence should include:

\- recruiter priority signals

\- evidence expectations





Alignment Report should include:

\- matched hiring signals

\- missing hiring signals

\- evidence strength





\## Frontend



Reuse existing pages.



Add display sections:

\- Hiring Signals

\- Evidence Strength



Do not redesign UI.





\## Constraints



\- Use structured local data.

\- No scraping.

\- No external APIs.

\- No secrets.

\- Keep architecture unchanged.



Verify:

\- backend compile check

\- npm.cmd run build

\# Hiring Signal Foundation



Goal:

Add recruitment signal intelligence to improve role matching accuracy.



Implemented:



\- Added local hiring signal dataset.

\- Added HiringSignalService.

\- Integrated hiring signals into Role Intelligence.

\- Integrated hiring signals into Alignment Report.

\- Added evidence strength evaluation.



Design:



Hiring signals connect:

Role requirements

\+

Recruitment priorities

\+

Candidate evidence



Constraints:

\- Local structured data.

\- No external APIs.

\- No scraping.

\- Reuse existing architecture.


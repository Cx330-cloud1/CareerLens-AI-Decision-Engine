Implement Role Intelligence and Alignment Foundation.



Goal:

Complete the first CareerLens end-to-end workflow:

Resume Intelligence -> Role Intelligence -> Alignment Report.



Current:

Resume Intelligence exists.

Frontend workspace exists.



Do:



\## Backend



Add role intelligence workflow.



Support:

\- target role input

\- JD text analysis



Create structured outputs:



Role:

\- role\_identity

\- responsibilities

\- required\_capabilities

\- hidden\_expectations

\- work\_context



Alignment:

\- overall\_fit

\- matched\_capabilities

\- capability\_gaps

\- evidence\_comparison

\- improvement\_actions





\## Frontend



Implement Role Intelligence page:



Show:

\- JD input

\- role summary

\- capability requirements

\- hidden expectations

\- work reality





Implement Match Report page:



Connect resume analysis and role analysis.



Show:

\- fit score

\- strengths

\- gaps

\- recommended actions





\## Data



Add minimal models:

\- RoleRequirement

\- AlignmentReport



Keep extensible for future LLM integration.





\## Constraints



\- Follow current Vue + FastAPI architecture.

\- Reuse existing design system.

\- Do not redesign UI.

\- Do not add external APIs.

\- Do not add secrets.

\- Use mock structured AI output.



Verify:

\- npm.cmd run build

\- backend compile check


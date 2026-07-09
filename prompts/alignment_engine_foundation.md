Implement Alignment Engine Foundation.



Goal:

Connect Talent Intelligence and Role Knowledge to generate explainable career alignment reports.



Current capabilities:

\- Resume Intelligence exists.

\- Role Knowledge Base exists.

\- Role Intelligence exists.



Build:



\## Backend



Add alignment service.



Input:

\- candidate profile

\- resume evidence

\- selected role template



Output:



alignment\_report:

\- overall\_score

\- confidence

\- matched\_capabilities

\- capability\_gaps

\- evidence\_mapping

\- recommended\_actions





Capability comparison should explain:

\- why a capability matches

\- what evidence supports it

\- what is missing





\## Frontend



Upgrade Match Report page into a professional alignment workspace.



Display:



1\. Overall alignment

\- score

\- confidence

\- summary



2\. Strengths

\- matched capabilities

\- supporting evidence



3\. Gaps

\- missing capabilities

\- impact level



4\. Actions

\- concrete improvement suggestions





\## Data



Add minimal models:

\- AlignmentReport

\- CapabilityMatch

\- GapAnalysis

\- EvidenceLink





\## Constraints



\- Reuse existing architecture.

\- Reuse current design system.

\- Do not redesign unrelated pages.

\- No external APIs.

\- No secrets.

\- Use structured mock analysis.





Verify:

\- frontend build

\- backend compile check




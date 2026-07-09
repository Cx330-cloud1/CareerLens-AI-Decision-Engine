Refine CareerLens frontend UI based on the current implementation.



Context:

CareerLens is an AI Talent-Role Alignment SaaS workspace.

The current redesign introduced a strong visual style, but the product now feels like a marketing website instead of an enterprise intelligence application.



Goal:

Transform the interface from "AI landing page" into a professional AI analysis workspace.



Important:

\- Do not redesign from scratch.

\- Reuse existing components and styles where possible.

\- Do not modify backend APIs.

\- Do not add unnecessary dependencies.

\- Do not create decorative UI without product value.



Product positioning:

CareerLens helps users understand:

1\. Who they are professionally.

2\. What roles fit them.

3\. Why they fit or do not fit.

4\. How to improve their positioning.



Design direction:

\- Enterprise SaaS

\- Intelligence workspace

\- Similar clarity to Linear, Notion, modern analytics platforms

\- Professional, calm, information-rich

\- Premium but practical



Avoid:

\- Landing page hero sections

\- Oversized marketing typography

\- Excessive empty space

\- Too many cards

\- Decorative animations

\- Generic AI dashboard patterns





Tasks:



\## 1. Global workspace refinement



Improve:

\- App shell

\- Sidebar

\- Page header

\- Content spacing

\- Typography hierarchy



Requirements:

\- Navigation should represent workflow stages:

&#x20; Dashboard

&#x20; Resume Intelligence

&#x20; Role Intelligence

&#x20; Alignment Report

&#x20; Career Strategy



\- Remove mixed Chinese-English labels.

\- Keep language switching support.



The user should feel they are entering a professional analysis environment, not a website.





\## 2. Dashboard redesign



Current issue:

Dashboard only presents system status.



Transform it into a career intelligence overview.



Display:



\- Current candidate profile status

\- Resume analysis status

\- Target role status

\- Latest alignment result

\- Main capability signals

\- Important capability gaps

\- Recommended next actions



Use:

\- Metric blocks

\- Compact sections

\- Clear information hierarchy



Avoid:

Large empty panels.





\## 3. Resume Intelligence refinement



The page should feel like a professional talent dossier.



Structure:



A. Candidate Identity

\- professional positioning

\- background summary

\- confidence level



B. Capability Map

Show:

\- capability category

\- confidence

\- evidence strength



C. Experience Evidence

For each experience:

\- what capability it demonstrates

\- evidence quality

\- possible role relevance



D. Improvement Queue

Prioritize:

\- missing evidence

\- weak descriptions

\- recommended improvements



The user should immediately understand:

"What makes me valuable?"

"What is missing?"





\## 4. Role Intelligence refinement



Transform the page from simple JD input into role analysis workspace.



Input remains:

\- target role

\- JD text



Output should prioritize:



Role Overview:

\- what this role actually does



Core Capabilities:

\- required technical skills

\- business skills

\- collaboration skills



Hidden Expectations:

\- implicit hiring signals

\- seniority expectations

\- practical requirements



Work Reality:

\- typical responsibilities

\- daily workflow understanding



The analysis result is more important than the input form.





\## 5. Component system refinement



Keep reusable components.



Improve:



\- WorkspacePanel

\- MetricBlock

\- EvidenceCard

\- ConfidenceIndicator

\- EmptyState



Rules:

\- Avoid every section becoming a card.

\- Use background, spacing, dividers, and hierarchy.

\- Reserve cards for meaningful information.





\## 6. Visual system



Use:



\- neutral professional palette

\- one primary accent color

\- clear contrast

\- strong typography hierarchy



Target:

Visual density: medium-high.

Information should be easy to scan.



Do not:

\- add gradients everywhere

\- add excessive shadows

\- add unnecessary animations





\## 7. Product states



Improve:



Empty state:

Explain next action.



Loading:

Show analysis progress structure.



Error:

Provide useful recovery action.



The product should feel reliable.





Verification:



\- npm.cmd run build

\- Do not modify backend files.


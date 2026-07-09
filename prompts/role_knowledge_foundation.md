Implement Role Knowledge Foundation based on current CareerLens architecture.



Goal:

Create a reusable role knowledge base and career exploration entry.



Product flow:

Career Explorer -> Role Template -> Role Intelligence -> Alignment Report.



Scope:



Backend:



Add role knowledge models:

\- CareerCategory

\- RoleTemplate

\- Capability

\- RoleCapabilityMapping



Each role template should support:

\- role identity

\- responsibilities

\- required capabilities

\- evidence examples

\- common gaps

\- development actions



Add role knowledge service.



Frontend:



Add Career Explorer workflow.



Users can:

\- browse career categories

\- search predefined roles

\- select a target role



Update Role Intelligence:

Support two inputs:

1\. Select predefined role template

2\. Paste custom JD



Reuse current design system.



Data:



Create seed data for several common internet roles.



Include categories:

\- Technology

\- Product

\- Data

\- Business



Do not:

\- scrape websites

\- add external APIs

\- add secrets

\- redesign unrelated UI



Keep architecture extensible for future company and market intelligence.



Verify:

\- npm.cmd run build

\- backend compile check


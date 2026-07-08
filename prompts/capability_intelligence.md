Upgrade CareerLens Talent Profile into a Capability Intelligence system.



Goal:



Transform simple profile analysis into evidence-based capability mapping.





Backend:



Create:



backend/app/schemas/capability.py





Define:



Capability:

\- name

\- category

\- level

\- confidence

\- evidence

\- gaps





Update profile analysis response:



Replace generic strengths/gaps with:



career\_identity

capabilities

evidence\_map

development\_gaps

recommended\_roles





Service:



Update mock analysis logic.



Generate structured capability assessment.



Example capability categories:



\- Technical Engineering

\- AI Application Development

\- Product Thinking

\- User Research

\- Communication





Frontend:



Update TalentProfile.vue result display.



Create:



Capability cards

Evidence sections

Development gap sections





Design:



Premium SaaS style.



Avoid chatbot style.



Make it look like professional career intelligence report.





Do not implement real LLM API yet.



After implementation:



Run:



npm.cmd run build



Fix all errors.


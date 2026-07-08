Implement CareerLens Talent Profile domain module.



Goal:



Create the first core product workflow:



User Profile Input

&#x20;       ↓

Profile Analysis

&#x20;       ↓

Structured Talent Profile





Backend:



Create:



app/api/profile.py



app/services/profile/service.py



app/schemas/profile.py





API:



POST /api/profile/analyze





Input:



{

&#x20;education,

&#x20;skills,

&#x20;projects,

&#x20;target\_roles

}





Output:



{

&#x20;career\_identity,

&#x20;capabilities,

&#x20;evidence,

&#x20;strengths,

&#x20;gaps,

&#x20;recommended\_roles

}





Use Pydantic models.



Do not call external LLM API yet.



Implement a structured mock analysis service.





Frontend:



Update TalentProfile.vue.



Add:



\- profile input form

\- analyze button

\- result cards





Product requirements:



The output should feel like a professional career intelligence report, not a chatbot response.





Engineering requirements:



\- Follow existing architecture

\- Keep frontend/backend separated

\- Run npm.cmd run build after changes

\- Fix all errors


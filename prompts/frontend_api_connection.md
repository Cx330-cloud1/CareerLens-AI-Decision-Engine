Implement frontend-backend API connection for CareerLens.



Current status:



Frontend:

Vue3 + TypeScript + Vite



Backend:

FastAPI



Backend health endpoint:



GET http://127.0.0.1:8000/api/health





Goal:



Connect Dashboard with backend status.





Requirements:



Frontend:



1\. Create:



frontend/src/services/api.ts





Responsibilities:

\- Centralize API requests

\- Use environment variable for API base URL





2\. Add:



frontend/.env.example





Content:



VITE\_API\_BASE\_URL=http://127.0.0.1:8000





3\. Update Dashboard.vue





Display:



CareerLens System Status



Backend:

Connected ✓





If request fails:



Backend:

Disconnected





Engineering requirements:



\- Use TypeScript

\- Separate API logic from UI components

\- Follow existing project structure

\- Do not modify backend





After implementation:



Run:



npm run build



Fix all frontend errors.


Complete frontend internationalization coverage for CareerLens.



Current status:



\- vue-i18n is already installed.

\- Language switching works in App.vue.

\- Some pages still contain hardcoded English text.





Task:



Review all frontend Vue pages:



frontend/src/pages/



Especially:



\- TalentProfile.vue

\- CompanyIntelligence.vue

\- RoleIntelligence.vue

\- MatchReport.vue

\- CareerPlan.vue

\- Dashboard.vue





Requirements:



1\. Replace all user-facing hardcoded text with i18n keys.



2\. Add missing translations into:



src/locales/zh-CN.ts

src/locales/en-US.ts





Translate all UI elements:



\- page titles

\- subtitles

\- labels

\- buttons

\- placeholders

\- status messages

\- empty states





Example:



Before:



<h1>Structured professional identity</h1>



After:



<h1>{{ t("profile.title") }}</h1>





3\. Keep:



\- file names unchanged

\- variable names unchanged

\- API unchanged

\- backend unchanged





4\. Maintain premium SaaS style:



Chinese:

简洁、专业、技术感



English:

professional global SaaS style





5\. Run:



npm.cmd run build



Fix all errors.


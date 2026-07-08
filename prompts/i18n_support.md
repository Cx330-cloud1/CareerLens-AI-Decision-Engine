Implement internationalization support for CareerLens frontend.



Goal:



Support Chinese and English language switching.



Requirements:



Technology:

\- Vue 3

\- TypeScript

\- vue-i18n





Create:



src/locales/

&#x20; zh-CN.ts

&#x20; en-US.ts



src/i18n/

&#x20; index.ts





Features:



1\. Add language switcher in the application header/sidebar.



Options:



中文

English





2\. Translate current navigation:



Dashboard

Talent Profile

Company Intelligence

Role Intelligence

Match Report

Career Plan





3\. Replace hardcoded UI text with i18n keys.



4\. Save selected language in localStorage.



5\. Default language:

\- Browser Chinese -> zh-CN

\- Otherwise -> en-US





Engineering requirements:



\- Keep file names and code variables in English.

\- Do not modify backend.

\- Run:



npm.cmd run build



Fix all errors.


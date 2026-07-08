import { createRouter, createWebHistory } from "vue-router";

import CareerPlan from "../pages/CareerPlan.vue";
import CompanyIntelligence from "../pages/CompanyIntelligence.vue";
import Dashboard from "../pages/Dashboard.vue";
import MatchReport from "../pages/MatchReport.vue";
import RoleIntelligence from "../pages/RoleIntelligence.vue";
import TalentProfile from "../pages/TalentProfile.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", name: "dashboard", component: Dashboard },
    { path: "/talent-profile", name: "talent-profile", component: TalentProfile },
    {
      path: "/company-intelligence",
      name: "company-intelligence",
      component: CompanyIntelligence
    },
    { path: "/role-intelligence", name: "role-intelligence", component: RoleIntelligence },
    { path: "/match-report", name: "match-report", component: MatchReport },
    { path: "/career-plan", name: "career-plan", component: CareerPlan }
  ]
});

export default router;

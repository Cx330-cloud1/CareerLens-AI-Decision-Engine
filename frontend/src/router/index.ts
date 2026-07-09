import { createRouter, createWebHistory } from "vue-router";

import CareerPlan from "../pages/CareerPlan.vue";
import CareerExplorer from "../pages/CareerExplorer.vue";
import CompanyIntelligence from "../pages/CompanyIntelligence.vue";
import Dashboard from "../pages/Dashboard.vue";
import MatchReport from "../pages/MatchReport.vue";
import RoleIntelligence from "../pages/RoleIntelligence.vue";
import ResumeOptimization from "../pages/ResumeOptimization.vue";
import TalentProfile from "../pages/TalentProfile.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", name: "dashboard", component: Dashboard },
    { path: "/career-explorer", name: "career-explorer", component: CareerExplorer },
    { path: "/talent-profile", name: "talent-profile", component: TalentProfile },
    {
      path: "/company-intelligence",
      name: "company-intelligence",
      component: CompanyIntelligence
    },
    { path: "/role-intelligence", name: "role-intelligence", component: RoleIntelligence },
    { path: "/match-report", name: "match-report", component: MatchReport },
    {
      path: "/resume-optimization",
      name: "resume-optimization",
      component: ResumeOptimization
    },
    { path: "/career-plan", name: "career-plan", component: CareerPlan }
  ]
});

export default router;

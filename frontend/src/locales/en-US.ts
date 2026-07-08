export default {
  navigation: {
    dashboard: "Dashboard",
    talentProfile: "Talent Profile",
    companyIntelligence: "Company Intelligence",
    roleIntelligence: "Role Intelligence",
    matchReport: "Match Report",
    careerPlan: "Career Plan"
  },
  language: {
    label: "Language",
    zhCN: "Chinese",
    enUS: "English"
  },
  pages: {
    dashboard: {
      eyebrow: "Dashboard",
      title: "CareerLens System Status",
      backend: "Backend:",
      connected: "Connected",
      disconnected: "Disconnected"
    },
    talentProfile: {
      eyebrow: "Talent Profile",
      title: "Structured professional identity",
      lede: "Foundation page for profile data, evidence, and versions.",
      fields: {
        education: {
          label: "Education",
          placeholder: "MSc Computer Science, University...\nData analytics certificate..."
        },
        skills: {
          label: "Skills",
          placeholder: "Python\nSQL\nMarket research\nStakeholder communication"
        },
        projects: {
          label: "Projects",
          placeholder: "Built a churn dashboard that reduced weekly reporting time by 40%..."
        },
        targetRoles: {
          label: "Target Roles",
          placeholder: "Data Analyst\nProduct Analyst\nBusiness Intelligence Analyst"
        }
      },
      actions: {
        analyze: "Analyze Profile",
        analyzing: "Analyzing..."
      },
      report: {
        ariaLabel: "Talent profile report",
        careerIdentity: "Career Identity",
        capabilities: "Capabilities",
        evidence: "Evidence",
        strengths: "Strengths",
        gaps: "Gaps",
        recommendedRoles: "Recommended Roles"
      },
      empty: {
        ariaLabel: "Report preview",
        title: "Structured Talent Profile",
        description:
          "Complete the inputs and run the analysis to generate a career identity, capability map, evidence summary, strengths, gaps, and recommended roles."
      },
      errors: {
        analysisFailed: "Profile analysis failed. Confirm the backend is running and try again."
      }
    },
    companyIntelligence: {
      eyebrow: "Company Intelligence",
      title: "Company and market context",
      lede: "Foundation page for company DNA and source-backed intelligence."
    },
    roleIntelligence: {
      eyebrow: "Role Intelligence",
      title: "Role expectations and signals",
      lede: "Foundation page for role templates, requirements, and evaluation signals."
    },
    matchReport: {
      eyebrow: "Match Report",
      title: "Explainable fit analysis",
      lede: "Foundation page for score dimensions, evidence, assumptions, and confidence."
    },
    careerPlan: {
      eyebrow: "Career Plan",
      title: "Action plan and preparation path",
      lede: "Foundation page for sequenced actions tied to match gaps."
    }
  }
};

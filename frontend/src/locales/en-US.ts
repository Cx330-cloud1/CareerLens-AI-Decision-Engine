export default {
  navigation: {
    dashboard: "Dashboard",
    talentProfile: "Resume Intelligence",
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
      eyebrow: "Resume Intelligence",
      title: "Resume evidence to capability analysis",
      lede: "Upload a resume or paste resume text to generate structured identity, capability, evidence, and improvement signals.",
      upload: {
        title: "Upload resume",
        description: "PDF, TXT, Markdown, DOC, or DOCX. Text files are parsed locally for this foundation workflow.",
        status: "Input status",
        emptyStatus: "Waiting for resume",
        readyStatus: "{name} ready",
        textReadyStatus: "Pasted text ready"
      },
      fields: {
        resumeText: {
          label: "Resume text",
          placeholder: "Paste resume text here to preview evidence extraction. PDF upload is accepted as an artifact; detailed PDF text extraction is a later service integration."
        }
      },
      actions: {
        analyze: "Analyze Resume",
        analyzing: "Analyzing..."
      },
      report: {
        ariaLabel: "Resume intelligence report",
        candidateIdentity: "Candidate Identity",
        capabilities: "Capabilities",
        evidence: "Experience Evidence",
        suggestions: "Improvement Suggestions"
      },
      empty: {
        ariaLabel: "Resume intelligence preview",
        title: "Structured Resume Intelligence",
        description:
          "Upload a resume or paste resume text to generate capability cards, evidence cards, confidence signals, and next-step recommendations."
      },
      errors: {
        analysisFailed: "Resume analysis failed. Confirm the backend is running and try again."
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

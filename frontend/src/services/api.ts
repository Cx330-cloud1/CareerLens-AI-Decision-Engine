const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? "http://127.0.0.1:8000";

type HealthResponse = {
  status?: string;
};

export type ProfileAnalysisRequest = {
  education: string[];
  skills: string[];
  projects: string[];
  target_roles: string[];
};

export type ProfileAnalysisResponse = {
  career_identity: string;
  capabilities: string[];
  evidence: string[];
  strengths: string[];
  gaps: string[];
  recommended_roles: string[];
};

export type ResumeUploadRequest = {
  file_name: string;
  content_type?: string;
  file_size: number;
  resume_text: string;
};

export type CandidateIdentity = {
  name?: string | null;
  headline: string;
  target_direction: string;
  summary: string;
  confidence: number;
};

export type CapabilityCard = {
  capability_id: string;
  name: string;
  category: string;
  level: string;
  confidence: number;
  rationale: string;
  evidence_ids: string[];
};

export type CapabilityEvidence = {
  evidence_id: string;
  excerpt: string;
  source_section: string;
  strength: string;
  confidence: number;
};

export type ImprovementSuggestion = {
  suggestion_id: string;
  title: string;
  rationale: string;
  priority: string;
  confidence: number;
};

export type ResumeAnalysisResponse = {
  resume_id: string;
  parsing_status: string;
  candidate_identity: CandidateIdentity;
  capabilities: CapabilityCard[];
  experience_evidence: CapabilityEvidence[];
  improvement_suggestions: ImprovementSuggestion[];
  model_metadata: Record<string, string>;
};

export type RoleAnalysisRequest = {
  job_description?: string;
  target_role?: string;
  role_template_id?: string;
};

export type RoleIdentity = {
  title: string;
  role_family: string;
  seniority: string;
  business_context: string;
  confidence: number;
};

export type RoleCapabilityRequirement = {
  requirement_id: string;
  name: string;
  category: string;
  importance: string;
  evidence_signal: string;
  confidence: number;
};

export type WorkContext = {
  environment: string;
  collaboration_model: string;
  pace: string;
  success_measures: string[];
};

export type RoleRequirement = {
  role_identity: RoleIdentity;
  responsibilities: string[];
  required_capabilities: RoleCapabilityRequirement[];
  hidden_expectations: string[];
  work_context: WorkContext;
  model_metadata: Record<string, string>;
};

export type RoleAnalysisResponse = RoleRequirement & {
  role_id: string;
  source: "custom_jd" | "role_template";
};

export type CareerCategory = {
  category_id: string;
  name: string;
  description: string;
  role_count: number;
};

export type Capability = {
  capability_id: string;
  name: string;
  category: string;
  description: string;
};

export type RoleCapabilityMapping = {
  mapping_id: string;
  capability: Capability;
  importance: string;
  evidence_examples: string[];
  common_gaps: string[];
  development_actions: string[];
  confidence: number;
};

export type RoleTemplate = {
  template_id: string;
  category_id: string;
  title: string;
  role_family: string;
  seniority: string;
  summary: string;
  business_context: string;
  responsibilities: string[];
  capability_mappings: RoleCapabilityMapping[];
  common_gaps: string[];
  development_actions: string[];
};

export type RoleTemplateListResponse = {
  categories: CareerCategory[];
  templates: RoleTemplate[];
};

export type CandidateCapabilityInput = {
  name: string;
  category?: string;
  evidence?: string;
  confidence?: number;
};

export type CandidateProfileInput = {
  headline?: string | null;
  target_direction?: string | null;
  capabilities: string[];
  evidence: string[];
};

export type AlignmentAnalysisRequest = {
  candidate_profile?: CandidateProfileInput;
  resume_evidence?: CapabilityEvidence[];
  selected_role_template?: RoleTemplate;
  role_requirement?: RoleRequirement;
  candidate_capabilities: CandidateCapabilityInput[];
};

export type EvidenceLink = {
  evidence_id: string;
  source_section: string;
  excerpt: string;
  relevance: string;
  confidence: number;
};

export type CapabilityMatch = {
  capability: string;
  category: string;
  score: number;
  confidence: number;
  why_it_matches: string;
  supporting_evidence: EvidenceLink[];
  missing_evidence?: string | null;
};

export type GapAnalysis = {
  capability: string;
  category: string;
  impact_level: string;
  what_is_missing: string;
  evidence_needed: string;
  recommended_action: string;
};

export type EvidenceMapping = {
  requirement: string;
  evidence_links: EvidenceLink[];
  assessment: string;
  confidence: number;
};

export type AlignmentReport = {
  overall_score: number;
  confidence: number;
  summary: string;
  matched_capabilities: CapabilityMatch[];
  capability_gaps: GapAnalysis[];
  evidence_mapping: EvidenceMapping[];
  recommended_actions: string[];
  model_metadata: Record<string, string>;
};

export type ResumeOptimizationRequest = {
  resume_evidence: CapabilityEvidence[];
  target_role: RoleRequirement;
  alignment_gaps: GapAnalysis[];
  alignment_report?: AlignmentReport | null;
};

export type CapabilityPriority = {
  capability: string;
  category: string;
  priority: string;
  reason: string;
  confidence: number;
};

export type EvidenceImprovement = {
  evidence_id: string;
  capability: string;
  current_signal: string;
  improvement: string;
  quality_target: string;
  confidence: number;
};

export type ExperienceReframing = {
  source_section: string;
  target_capability: string;
  framing_guidance: string;
  before_signal: string;
  after_positioning: string;
};

export type MissingEvidence = {
  capability: string;
  evidence_needed: string;
  suggested_proof: string;
  impact_level: string;
};

export type ResumeOptimization = {
  capability_priorities: CapabilityPriority[];
  evidence_improvements: EvidenceImprovement[];
  experience_reframing: ExperienceReframing[];
  missing_evidence: MissingEvidence[];
};

export type ResumeOptimizationResponse = {
  resume_optimization: ResumeOptimization;
  model_metadata: Record<string, string>;
};

export type CareerStrategyRequest = {
  resume_optimization: ResumeOptimization;
  target_role: RoleRequirement;
  alignment_report?: AlignmentReport | null;
};

export type CareerAction = {
  title: string;
  rationale: string;
  evidence_outcome: string;
  priority: string;
};

export type RecommendedProject = {
  title: string;
  target_capabilities: string[];
  evidence_to_create: string;
  scope: string;
};

export type GrowthPathStep = {
  capability: string;
  current_gap: string;
  next_level_signal: string;
  validation_method: string;
};

export type CareerPlan = {
  short_term_actions: CareerAction[];
  medium_term_actions: CareerAction[];
  recommended_projects: RecommendedProject[];
  capability_growth_path: GrowthPathStep[];
};

export type CareerStrategyResponse = {
  career_plan: CareerPlan;
  model_metadata: Record<string, string>;
};

async function request<T>(path: string, options?: RequestInit): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${path}`, {
    headers: {
      "Content-Type": "application/json",
      ...options?.headers
    },
    ...options
  });

  if (!response.ok) {
    throw new Error(`API request failed with status ${response.status}`);
  }

  return response.json() as Promise<T>;
}

export async function getBackendHealth(): Promise<HealthResponse> {
  return request<HealthResponse>("/api/health");
}

export async function analyzeProfile(
  payload: ProfileAnalysisRequest
): Promise<ProfileAnalysisResponse> {
  return request<ProfileAnalysisResponse>("/api/profile/analyze", {
    method: "POST",
    body: JSON.stringify(payload)
  });
}

export async function analyzeResume(
  payload: ResumeUploadRequest
): Promise<ResumeAnalysisResponse> {
  return request<ResumeAnalysisResponse>("/api/resumes/analyze", {
    method: "POST",
    body: JSON.stringify(payload)
  });
}

export async function analyzeRole(
  payload: RoleAnalysisRequest
): Promise<RoleAnalysisResponse> {
  return request<RoleAnalysisResponse>("/api/roles/analyze", {
    method: "POST",
    body: JSON.stringify(payload)
  });
}

export async function getRoleTemplates(params?: {
  query?: string;
  category_id?: string;
}): Promise<RoleTemplateListResponse> {
  const searchParams = new URLSearchParams();
  if (params?.query) {
    searchParams.set("query", params.query);
  }
  if (params?.category_id) {
    searchParams.set("category_id", params.category_id);
  }
  const suffix = searchParams.toString() ? `?${searchParams.toString()}` : "";
  return request<RoleTemplateListResponse>(`/api/roles/templates${suffix}`);
}

export async function analyzeAlignment(
  payload: AlignmentAnalysisRequest
): Promise<AlignmentReport> {
  return request<AlignmentReport>("/api/matching/analyze", {
    method: "POST",
    body: JSON.stringify(payload)
  });
}

export async function optimizeResume(
  payload: ResumeOptimizationRequest
): Promise<ResumeOptimizationResponse> {
  return request<ResumeOptimizationResponse>("/api/resumes/optimize", {
    method: "POST",
    body: JSON.stringify(payload)
  });
}

export async function generateCareerStrategy(
  payload: CareerStrategyRequest
): Promise<CareerStrategyResponse> {
  return request<CareerStrategyResponse>("/api/career-strategy/generate", {
    method: "POST",
    body: JSON.stringify(payload)
  });
}

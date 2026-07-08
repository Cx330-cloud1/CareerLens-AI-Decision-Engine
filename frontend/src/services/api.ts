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

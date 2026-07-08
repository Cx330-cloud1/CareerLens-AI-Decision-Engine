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

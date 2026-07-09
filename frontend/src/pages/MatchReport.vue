<template>
  <section class="page-section match-page">
    <header class="page-header match-header">
      <div class="page-header__meta">
        <span class="status-token status-token--neutral">Alignment engine</span>
        <span v-if="roleRequirement" class="status-token">{{ roleRequirement.role_identity.title }}</span>
      </div>
      <h1>Career alignment workspace</h1>
      <p class="lede">
        Connect resume evidence and role knowledge into an explainable readiness report.
      </p>
    </header>

    <div class="match-workspace">
      <aside class="control-rail" aria-label="Alignment inputs">
        <WorkspacePanel class="input-panel">
          <div v-if="roleRequirement" class="role-summary">
            <span class="section-kicker">Selected role</span>
            <h2>{{ roleRequirement.role_identity.title }}</h2>
            <p>
              {{ roleRequirement.role_identity.seniority }}
              {{ roleRequirement.role_identity.role_family }} with
              {{ roleRequirement.required_capabilities.length }} capability requirements.
            </p>
          </div>

          <div v-else class="role-summary role-summary--warning">
            <span class="section-kicker">Role required</span>
            <p>Analyze a role before generating an alignment report.</p>
          </div>

          <div class="source-grid">
            <MetricBlock
              label="Resume evidence"
              :value="latestResume?.experience_evidence.length ?? 0"
              detail="evidence records"
              variant="muted"
            />
            <MetricBlock
              label="Candidate signals"
              :value="parsedCapabilityCount"
              detail="capability lines"
              variant="muted"
            />
          </div>

          <label class="field-group">
            <span>Candidate capabilities</span>
            <textarea
              v-model="candidateCapabilityText"
              rows="12"
              placeholder="Paste capability lines from Resume Intelligence, one per line. Include evidence or project context when possible."
            />
          </label>

          <button class="primary-button" type="button" :disabled="isAnalyzing || !canAnalyze" @click="handleAnalyze">
            {{ isAnalyzing ? "Analyzing..." : "Generate alignment report" }}
          </button>

          <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
        </WorkspacePanel>
      </aside>

      <main class="report-panel" aria-label="Candidate-role alignment report">
        <template v-if="report">
          <section class="overview-grid" aria-label="Overall alignment">
            <WorkspacePanel class="score-panel" variant="accent">
              <span class="section-kicker">Overall alignment</span>
              <div class="score-panel__body">
                <strong>{{ Math.round(report.overall_score) }}</strong>
                <span>/100</span>
              </div>
              <p>{{ report.summary }}</p>
            </WorkspacePanel>

            <MetricBlock
              label="Confidence"
              :value="`${Math.round(report.confidence * 100)}%`"
              :detail="confidenceLabel"
            />
            <MetricBlock
              label="Strengths"
              :value="report.matched_capabilities.length"
              detail="matched capabilities"
            />
            <MetricBlock
              label="Gaps"
              :value="report.capability_gaps.length"
              detail="development areas"
              :variant="report.capability_gaps.length ? 'danger' : 'muted'"
            />
          </section>

          <section class="alignment-columns">
            <WorkspacePanel class="analysis-section">
              <div class="section-heading">
                <span class="section-kicker">Strengths</span>
                <strong>{{ report.matched_capabilities.length }}</strong>
              </div>
              <article
                v-for="match in report.matched_capabilities"
                :key="match.capability"
                class="alignment-item"
              >
                <div class="card-topline">
                  <h3>{{ match.capability }}</h3>
                  <span>{{ Math.round(match.score) }}</span>
                </div>
                <p>{{ match.why_it_matches }}</p>
                <div class="evidence-strip">
                  <span
                    v-for="evidence in match.supporting_evidence"
                    :key="evidence.evidence_id"
                  >
                    {{ evidence.source_section }}: {{ evidence.excerpt }}
                  </span>
                </div>
                <small v-if="match.missing_evidence">{{ match.missing_evidence }}</small>
              </article>
              <p v-if="!report.matched_capabilities.length" class="quiet-note">
                No strengths met the evidence threshold yet.
              </p>
            </WorkspacePanel>

            <WorkspacePanel class="analysis-section">
              <div class="section-heading">
                <span class="section-kicker">Gaps</span>
                <strong>{{ report.capability_gaps.length }}</strong>
              </div>
              <article
                v-for="gap in report.capability_gaps"
                :key="gap.capability"
                class="alignment-item alignment-item--gap"
              >
                <div class="card-topline">
                  <h3>{{ gap.capability }}</h3>
                  <span>{{ gap.impact_level }}</span>
                </div>
                <p>{{ gap.what_is_missing }}</p>
                <small>{{ gap.evidence_needed }}</small>
              </article>
              <p v-if="!report.capability_gaps.length" class="quiet-note">
                No major capability gaps were detected from the supplied evidence.
              </p>
            </WorkspacePanel>
          </section>

          <section class="lower-grid">
            <WorkspacePanel class="analysis-section">
              <div class="section-heading">
                <span class="section-kicker">Evidence mapping</span>
                <strong>{{ report.evidence_mapping.length }}</strong>
              </div>
              <article
                v-for="mapping in report.evidence_mapping"
                :key="mapping.requirement"
                class="mapping-row"
              >
                <div>
                  <h3>{{ mapping.requirement }}</h3>
                  <p>{{ mapping.assessment }}</p>
                </div>
                <span>{{ Math.round(mapping.confidence * 100) }}%</span>
              </article>
            </WorkspacePanel>

            <WorkspacePanel class="analysis-section action-section" variant="accent">
              <div class="section-heading">
                <span class="section-kicker">Actions</span>
                <strong>{{ report.recommended_actions.length }}</strong>
              </div>
              <ol>
                <li v-for="action in report.recommended_actions" :key="action">
                  {{ action }}
                </li>
              </ol>
            </WorkspacePanel>
          </section>
        </template>

        <WorkspacePanel v-else class="empty-state">
          <span class="section-kicker">Explainable report</span>
          <h2>Generate an alignment report from the saved role and resume evidence.</h2>
          <p>
            The report will show overall score, confidence, matched capabilities,
            capability gaps, evidence links, and targeted improvement actions.
          </p>
        </WorkspacePanel>
      </main>
    </div>
  </section>
</template>

<script setup lang="ts">
import { computed, ref } from "vue";

import MetricBlock from "../components/MetricBlock.vue";
import WorkspacePanel from "../components/WorkspacePanel.vue";
import {
  analyzeAlignment,
  type AlignmentReport,
  type CandidateCapabilityInput,
  type CandidateProfileInput,
  type ResumeAnalysisResponse,
  type RoleAnalysisResponse,
  type RoleRequirement
} from "../services/api";

const ROLE_STORAGE_KEY = "careerlens.latestRoleRequirement";
const RESUME_STORAGE_KEY = "careerlens.latestResumeAnalysis";
const ALIGNMENT_STORAGE_KEY = "careerlens.latestAlignmentReport";

const roleRequirement = ref<RoleAnalysisResponse | null>(loadSavedRole());
const latestResume = ref<ResumeAnalysisResponse | null>(loadSavedResume());
const candidateCapabilityText = ref(buildCapabilityText(latestResume.value));
const report = ref<AlignmentReport | null>(null);
const isAnalyzing = ref(false);
const errorMessage = ref("");

const parsedCapabilityCount = computed(() => {
  return parseCandidateCapabilities(candidateCapabilityText.value).length;
});

const canAnalyze = computed(() => {
  return Boolean(roleRequirement.value && candidateCapabilityText.value.trim());
});

const confidenceLabel = computed(() => {
  if (!report.value) {
    return "Not analyzed";
  }

  if (report.value.confidence >= 0.76) {
    return "high confidence";
  }

  if (report.value.confidence >= 0.58) {
    return "medium confidence";
  }

  return "low confidence";
});

const handleAnalyze = async () => {
  if (!roleRequirement.value) {
    errorMessage.value = "Analyze a role before creating an alignment report.";
    return;
  }

  isAnalyzing.value = true;
  errorMessage.value = "";

  try {
    report.value = await analyzeAlignment({
      role_requirement: toRoleRequirement(roleRequirement.value),
      candidate_profile: toCandidateProfile(latestResume.value),
      resume_evidence: latestResume.value?.experience_evidence ?? [],
      candidate_capabilities: parseCandidateCapabilities(candidateCapabilityText.value)
    });
    localStorage.setItem(ALIGNMENT_STORAGE_KEY, JSON.stringify(report.value));
  } catch {
    errorMessage.value = "Alignment analysis failed. Confirm the backend is running and try again.";
  } finally {
    isAnalyzing.value = false;
  }
};

function loadSavedRole(): RoleAnalysisResponse | null {
  const rawValue = localStorage.getItem(ROLE_STORAGE_KEY);
  if (!rawValue) {
    return null;
  }

  try {
    return normalizeRoleAnalysis(JSON.parse(rawValue));
  } catch {
    return null;
  }
}

function loadSavedResume(): ResumeAnalysisResponse | null {
  const rawValue = localStorage.getItem(RESUME_STORAGE_KEY);
  if (!rawValue) {
    return null;
  }

  try {
    return JSON.parse(rawValue) as ResumeAnalysisResponse;
  } catch {
    return null;
  }
}

function toRoleRequirement(role: RoleAnalysisResponse): RoleRequirement {
  return {
    role_identity: role.role_identity,
    responsibilities: role.responsibilities,
    required_capabilities: role.required_capabilities,
    hidden_expectations: role.hidden_expectations,
    work_context: role.work_context,
    model_metadata: role.model_metadata
  };
}

function toCandidateProfile(resume: ResumeAnalysisResponse | null): CandidateProfileInput | undefined {
  if (!resume) {
    return undefined;
  }

  return {
    headline: resume.candidate_identity.headline,
    target_direction: resume.candidate_identity.target_direction,
    capabilities: resume.capabilities.map((capability) => capability.name),
    evidence: resume.experience_evidence.map((item) => item.excerpt)
  };
}

function normalizeRoleAnalysis(value: unknown): RoleAnalysisResponse | null {
  if (!value || typeof value !== "object") {
    return null;
  }

  const role = value as RoleAnalysisResponse & {
    hidden_requirements?: string[];
    work_context?: RoleAnalysisResponse["work_context"];
  };

  return {
    ...role,
    hidden_expectations: role.hidden_expectations ?? role.hidden_requirements ?? [],
    work_context: role.work_context ?? {
      environment: role.role_identity?.business_context ?? "Technology role context.",
      collaboration_model: "Cross-functional collaboration with stakeholders and delivery partners.",
      pace: "Moderate delivery cadence with discovery and execution cycles.",
      success_measures: role.responsibilities?.slice(0, 3) ?? []
    }
  };
}

function parseCandidateCapabilities(value: string): CandidateCapabilityInput[] {
  return value
    .split(/\r?\n/)
    .map((line) => line.trim())
    .filter(Boolean)
    .map((line, index) => {
      const [name, ...evidenceParts] = line.split(":");
      return {
        name: name || `Capability ${index + 1}`,
        evidence: evidenceParts.join(":").trim() || line,
        confidence: 0.68
      };
    });
}

function buildCapabilityText(resume: ResumeAnalysisResponse | null): string {
  if (!resume) {
    return "";
  }

  return resume.capabilities
    .map((capability) => {
      const evidence = resume.experience_evidence
        .filter((item) => capability.evidence_ids.includes(item.evidence_id))
        .map((item) => item.excerpt)
        .join(" ");

      return `${capability.name}: ${capability.rationale} ${evidence}`.trim();
    })
    .join("\n");
}
</script>

<style scoped>
.match-page {
  max-width: 1240px;
}

.match-header {
  margin-bottom: 24px;
}

.match-workspace {
  display: grid;
  grid-template-columns: minmax(300px, 390px) minmax(0, 1fr);
  gap: 18px;
  align-items: start;
}

.control-rail {
  position: sticky;
  top: 18px;
}

.input-panel,
.analysis-section,
.score-panel {
  padding: 18px;
}

.input-panel {
  display: grid;
  gap: 16px;
}

.role-summary {
  display: grid;
  gap: 8px;
}

.role-summary p,
.score-panel p,
.alignment-item p,
.alignment-item small,
.mapping-row p,
.quiet-note {
  margin: 0;
  color: var(--text-muted);
  font-size: 14px;
  line-height: 1.55;
}

.role-summary--warning {
  border-radius: 8px;
  background: #fbf3db;
  padding: 12px;
}

.source-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 10px;
}

.report-panel {
  display: grid;
  gap: 14px;
  min-width: 0;
}

.overview-grid {
  display: grid;
  grid-template-columns: minmax(260px, 1.4fr) repeat(3, minmax(130px, 0.7fr));
  gap: 12px;
}

.score-panel {
  display: grid;
  gap: 14px;
}

.score-panel__body {
  display: flex;
  align-items: baseline;
  gap: 8px;
}

.score-panel__body strong {
  color: var(--text);
  font-size: clamp(44px, 6vw, 72px);
  font-weight: 780;
  letter-spacing: -0.04em;
  line-height: 0.9;
  font-variant-numeric: tabular-nums;
}

.score-panel__body span {
  color: var(--text-muted);
  font-size: 18px;
  font-weight: 700;
}

.alignment-columns,
.lower-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 14px;
}

.analysis-section {
  display: grid;
  gap: 12px;
  align-content: start;
}

.alignment-item {
  display: grid;
  gap: 10px;
  border-top: 1px solid var(--border);
  padding-top: 12px;
}

.alignment-item--gap .card-topline span {
  background: #fdebec;
  color: #9f2f2d;
}

.evidence-strip {
  display: grid;
  gap: 7px;
}

.evidence-strip span {
  border-left: 2px solid #cfddcd;
  color: #4d504b;
  font-size: 13px;
  line-height: 1.45;
  padding-left: 10px;
}

.mapping-row {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 14px;
  align-items: start;
  border-top: 1px solid var(--border);
  padding-top: 12px;
}

.mapping-row span {
  color: var(--accent);
  font-size: 13px;
  font-weight: 780;
  font-variant-numeric: tabular-nums;
}

.action-section ol {
  display: grid;
  gap: 10px;
  margin: 0;
  padding-left: 20px;
}

.action-section li {
  color: #384038;
  font-size: 14px;
  line-height: 1.55;
  padding-left: 4px;
}

@media (max-width: 1100px) {
  .match-workspace,
  .overview-grid,
  .alignment-columns,
  .lower-grid {
    grid-template-columns: 1fr;
  }

  .control-rail {
    position: static;
  }
}

@media (max-width: 640px) {
  .source-grid {
    grid-template-columns: 1fr;
  }

  .input-panel,
  .analysis-section,
  .score-panel {
    padding: 16px;
  }
}
</style>

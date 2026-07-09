<template>
  <section class="page-section dashboard-page">
    <header class="page-header dashboard-hero">
      <div class="page-header__meta">
        <span class="status-token">Workspace</span>
        <span :class="['status-token', backendConnected ? '' : 'status-token--danger']">
          {{ backendConnected ? "Backend connected" : "Backend unavailable" }}
        </span>
      </div>
      <h1>Career intelligence overview</h1>
      <p class="lede">
        Track the candidate evidence base, active target role, confidence signals, and the next
        decisions needed to move from profile input to explainable fit analysis.
      </p>
    </header>

    <div class="metric-grid">
      <MetricBlock
        label="Candidate profile"
        :value="candidateStatus"
        :detail="candidateDetail"
        :variant="resumeAnalysis ? 'accent' : 'muted'"
      />
      <MetricBlock
        label="Active target role"
        :value="roleTitle"
        :detail="roleDetail"
        :variant="roleRequirement ? 'accent' : 'muted'"
      />
      <MetricBlock
        label="Evidence strength"
        :value="evidenceStrength"
        :detail="`${evidenceCount} evidence cards available`"
      />
      <MetricBlock
        label="Analysis confidence"
        :value="confidenceLabel"
        :detail="analysisState"
      />
      <MetricBlock
        label="Latest alignment"
        :value="alignmentStatus"
        :detail="alignmentDetail"
        :variant="resumeAnalysis && roleRequirement ? 'accent' : 'muted'"
      />
    </div>

    <div class="dashboard-grid">
      <WorkspacePanel class="workspace-brief">
        <div class="section-heading">
          <span class="section-kicker">Latest analysis state</span>
          <strong>{{ analysisState }}</strong>
        </div>

        <div v-if="resumeAnalysis" class="candidate-summary">
          <div>
            <h2>{{ resumeAnalysis.candidate_identity.headline }}</h2>
            <p>{{ resumeAnalysis.candidate_identity.summary }}</p>
          </div>
          <ConfidenceMeter
            :value="resumeAnalysis.candidate_identity.confidence"
            label="Identity confidence"
          />
        </div>

        <EmptyState
          v-else
          eyebrow="No candidate profile"
          title="Analyze a resume to populate the workspace"
          description="The dashboard will show candidate identity, capability signals, evidence strength, gaps, and next actions once Resume Intelligence has a result."
        />
      </WorkspacePanel>

      <WorkspacePanel class="next-actions">
        <div class="section-heading">
          <span class="section-kicker">Next actions</span>
          <strong>{{ nextActions.length }}</strong>
        </div>
        <ol>
          <li v-for="action in nextActions" :key="action.title">
            <span>{{ action.step }}</span>
            <div>
              <strong>{{ action.title }}</strong>
              <p>{{ action.detail }}</p>
            </div>
          </li>
        </ol>
      </WorkspacePanel>

      <WorkspacePanel class="capability-board">
        <div class="section-heading">
          <span class="section-kicker">Key capability signals</span>
          <strong>{{ topCapabilities.length }}</strong>
        </div>
        <div v-if="topCapabilities.length" class="signal-list">
          <article
            v-for="capability in topCapabilities"
            :key="capability.capability_id"
            class="signal-row"
          >
            <div>
              <h3>{{ capability.name }}</h3>
              <p>{{ capability.rationale }}</p>
              <div class="tag-row">
                <span>{{ capability.category }}</span>
                <span>{{ capability.level }}</span>
              </div>
            </div>
            <ConfidenceMeter :value="capability.confidence" label="Signal confidence" />
          </article>
        </div>
        <EmptyState
          v-else
          eyebrow="Signal board"
          title="Capability map is waiting"
          description="Upload a resume to generate capability cards with rationale and confidence."
        />
      </WorkspacePanel>

      <WorkspacePanel class="gap-board">
        <div class="section-heading">
          <span class="section-kicker">Major gaps</span>
          <strong>{{ gapItems.length }}</strong>
        </div>
        <div v-if="gapItems.length" class="gap-list">
          <article v-for="gap in gapItems" :key="gap.title">
            <span class="status-token status-token--neutral">{{ gap.priority }}</span>
            <h3>{{ gap.title }}</h3>
            <p>{{ gap.rationale }}</p>
          </article>
        </div>
        <EmptyState
          v-else
          eyebrow="Gap review"
          title="No improvement priorities yet"
          description="Resume Intelligence will surface missing evidence and priority improvements after analysis."
        />
      </WorkspacePanel>
    </div>
  </section>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from "vue";

import ConfidenceMeter from "../components/ConfidenceMeter.vue";
import EmptyState from "../components/EmptyState.vue";
import MetricBlock from "../components/MetricBlock.vue";
import WorkspacePanel from "../components/WorkspacePanel.vue";
import {
  getBackendHealth,
  type ResumeAnalysisResponse,
  type RoleAnalysisResponse
} from "../services/api";

const RESUME_STORAGE_KEY = "careerlens.latestResumeAnalysis";
const ROLE_STORAGE_KEY = "careerlens.latestRoleRequirement";

const backendConnected = ref(false);
const resumeAnalysis = ref<ResumeAnalysisResponse | null>(loadStored<ResumeAnalysisResponse>(RESUME_STORAGE_KEY));
const roleRequirement = ref<RoleAnalysisResponse | null>(loadStored<RoleAnalysisResponse>(ROLE_STORAGE_KEY));

onMounted(async () => {
  resumeAnalysis.value = loadStored<ResumeAnalysisResponse>(RESUME_STORAGE_KEY);
  roleRequirement.value = loadStored<RoleAnalysisResponse>(ROLE_STORAGE_KEY);

  try {
    await getBackendHealth();
    backendConnected.value = true;
  } catch {
    backendConnected.value = false;
  }
});

const candidateStatus = computed(() => (resumeAnalysis.value ? "Ready" : "Missing"));
const candidateDetail = computed(() => {
  if (!resumeAnalysis.value) {
    return "Resume intelligence has not run";
  }

  return `${resumeAnalysis.value.capabilities.length} capabilities mapped`;
});

const roleTitle = computed(() => roleRequirement.value?.role_identity.title ?? "Not set");
const roleDetail = computed(() => {
  if (!roleRequirement.value) {
    return "Analyze a JD to activate matching";
  }

  return `${roleRequirement.value.role_identity.seniority} ${roleRequirement.value.role_identity.role_family}`;
});

const evidenceCount = computed(() => resumeAnalysis.value?.experience_evidence.length ?? 0);
const evidenceStrength = computed(() => {
  if (!resumeAnalysis.value || evidenceCount.value === 0) {
    return "No signal";
  }

  const strongCount = resumeAnalysis.value.experience_evidence.filter((item) =>
    item.strength.toLowerCase().includes("strong")
  ).length;

  return strongCount > 0 ? `${strongCount} strong` : "Mixed";
});

const confidenceLabel = computed(() => {
  const value = resumeAnalysis.value?.candidate_identity.confidence;
  return typeof value === "number" ? `${Math.round(value * 100)}%` : "Pending";
});

const alignmentStatus = computed(() => {
  if (resumeAnalysis.value && roleRequirement.value) {
    return "Ready";
  }

  return "Not generated";
});

const alignmentDetail = computed(() => {
  if (!resumeAnalysis.value || !roleRequirement.value) {
    return "Requires candidate profile and target role";
  }

  return "Generate fit rationale from Alignment Report";
});

const analysisState = computed(() => {
  if (!backendConnected.value) {
    return "Connection check needed";
  }

  return resumeAnalysis.value ? "Resume intelligence ready" : "Waiting for input";
});

const topCapabilities = computed(() => {
  return [...(resumeAnalysis.value?.capabilities ?? [])]
    .sort((left, right) => right.confidence - left.confidence)
    .slice(0, 4);
});

const gapItems = computed(() => {
  return (resumeAnalysis.value?.improvement_suggestions ?? []).slice(0, 4).map((suggestion) => ({
    title: suggestion.title,
    rationale: suggestion.rationale,
    priority: suggestion.priority
  }));
});

const nextActions = computed(() => {
  const actions = [];

  if (!resumeAnalysis.value) {
    actions.push({
      step: "01",
      title: "Run Resume Intelligence",
      detail: "Create candidate identity, capabilities, evidence cards, and confidence signals."
    });
  }

  if (!roleRequirement.value) {
    actions.push({
      step: "02",
      title: "Analyze the target role",
      detail: "Turn the JD into required capabilities, responsibilities, and hidden expectations."
    });
  }

  if (resumeAnalysis.value && roleRequirement.value) {
    actions.push({
      step: "03",
      title: "Generate match report",
      detail: "Compare candidate signals against role requirements with explainable gaps."
    });
  }

  if (resumeAnalysis.value?.improvement_suggestions.length) {
    actions.push({
      step: "04",
      title: "Address priority gaps",
      detail: "Strengthen the highest-priority evidence gaps before outreach or interviews."
    });
  }

  return actions;
});

function loadStored<T>(key: string): T | null {
  const rawValue = localStorage.getItem(key);
  if (!rawValue) {
    return null;
  }

  try {
    return JSON.parse(rawValue) as T;
  } catch {
    return null;
  }
}
</script>

<style scoped>
.dashboard-page {
  display: grid;
  gap: 22px;
}

.dashboard-hero {
  max-width: 900px;
}

.dashboard-grid {
  display: grid;
  grid-template-columns: minmax(0, 1.35fr) minmax(300px, 0.65fr);
  gap: 14px;
  align-items: start;
}

.workspace-brief,
.capability-board,
.gap-board,
.next-actions {
  display: grid;
  gap: 18px;
  padding: 22px;
}

.workspace-brief {
  min-height: 410px;
}

.candidate-summary {
  display: grid;
  gap: 22px;
  align-content: start;
}

.candidate-summary p,
.signal-row p,
.gap-list p,
.next-actions p {
  margin: 0;
  color: var(--text-muted);
  font-size: 14px;
  line-height: 1.6;
}

.candidate-summary p {
  max-width: 72ch;
  font-size: 16px;
}

.next-actions ol {
  display: grid;
  gap: 14px;
  margin: 0;
  padding: 0;
  list-style: none;
}

.next-actions li {
  display: grid;
  grid-template-columns: 34px 1fr;
  gap: 12px;
}

.next-actions li > span {
  color: var(--text-soft);
  font-size: 11px;
  font-weight: 800;
  font-variant-numeric: tabular-nums;
}

.next-actions strong {
  display: block;
  margin-bottom: 4px;
  color: var(--text);
  font-size: 14px;
}

.capability-board {
  grid-column: 1 / -1;
}

.signal-list {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 12px;
}

.signal-row {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 180px;
  gap: 18px;
  border: 1px solid var(--border);
  border-radius: 10px;
  background: #fffefa;
  padding: 16px;
}

.signal-row h3,
.gap-list h3 {
  margin-bottom: 7px;
}

.signal-row .tag-row {
  margin-top: 12px;
}

.gap-list {
  display: grid;
  gap: 12px;
}

.gap-list article {
  display: grid;
  gap: 9px;
  border-top: 1px solid var(--border);
  padding-top: 14px;
}

.gap-list article:first-child {
  border-top: 0;
  padding-top: 0;
}

@media (max-width: 1100px) {
  .dashboard-grid,
  .signal-list,
  .signal-row {
    grid-template-columns: 1fr;
  }
}
</style>

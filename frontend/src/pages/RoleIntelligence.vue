<template>
  <section class="page-section role-page">
    <header class="page-header role-header">
      <div class="page-header__meta">
        <span class="status-token">Role Intelligence</span>
        <span :class="['status-token', analysis ? '' : 'status-token--neutral']">
          {{ analysis ? "Requirement object ready" : "Awaiting JD" }}
        </span>
      </div>
      <h1>Turn a job description into a role intelligence brief</h1>
      <p class="lede">
        Extract what the role does, which capabilities matter, what hiring teams imply but do not
        state, and how the work is likely to operate day to day.
      </p>
    </header>

    <div class="role-workspace">
      <WorkspacePanel class="input-panel">
        <div class="panel-heading">
          <span class="section-kicker">Role input</span>
          <strong>{{ inputStatus }}</strong>
        </div>

        <form @submit.prevent="handleAnalyze">
          <div class="mode-switch" aria-label="Role input mode">
            <button
              type="button"
              :class="{ active: inputMode === 'template' }"
              @click="inputMode = 'template'"
            >
              Role template
            </button>
            <button
              type="button"
              :class="{ active: inputMode === 'custom' }"
              @click="inputMode = 'custom'"
            >
              Custom JD
            </button>
          </div>

          <template v-if="inputMode === 'template'">
            <label class="field-group">
              <span>Predefined role</span>
              <select v-model="selectedTemplateId">
                <option value="">Select a role template</option>
                <option
                  v-for="template in roleTemplates"
                  :key="template.template_id"
                  :value="template.template_id"
                >
                  {{ template.title }} · {{ template.role_family }}
                </option>
              </select>
            </label>

            <div v-if="selectedTemplate" class="template-preview">
              <span class="section-kicker">{{ selectedTemplate.seniority }} template</span>
              <strong>{{ selectedTemplate.title }}</strong>
              <p>{{ selectedTemplate.summary }}</p>
              <div class="tag-row">
                <span>{{ selectedTemplate.capability_mappings.length }} capabilities</span>
                <span>{{ selectedTemplate.responsibilities.length }} responsibilities</span>
              </div>
            </div>
          </template>

          <template v-else>
            <label class="field-group">
              <span>Target role</span>
              <input
                v-model="targetRole"
                placeholder="AI Product Analyst, Data Analyst, Backend Engineer"
              />
            </label>

            <label class="field-group">
              <span>Job description</span>
              <textarea
                v-model="jobDescription"
                rows="14"
                placeholder="Paste the JD, responsibilities, requirements, and company context here."
              />
            </label>
          </template>

          <button class="primary-button" type="submit" :disabled="isAnalyzing || !canAnalyze">
            {{ isAnalyzing ? "Analyzing role..." : "Analyze role" }}
          </button>

          <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
        </form>
      </WorkspacePanel>

      <section v-if="analysis" class="report-panel" aria-label="Role intelligence report">
        <WorkspacePanel class="role-overview">
          <div class="role-overview__header">
            <div>
              <span class="section-kicker">Role overview</span>
              <h2>{{ analysis.role_identity.title }}</h2>
            </div>
            <span class="confidence-badge">
              {{ formatConfidence(analysis.role_identity.confidence) }}
            </span>
          </div>
          <span :class="['status-token', analysis.source === 'role_template' ? '' : 'status-token--neutral']">
            {{ analysis.source === "role_template" ? "Template source" : "Custom JD source" }}
          </span>
          <p>{{ analysis.role_identity.business_context }}</p>
          <div class="identity-grid">
            <div>
              <span>Role family</span>
              <strong>{{ analysis.role_identity.role_family }}</strong>
            </div>
            <div>
              <span>Seniority</span>
              <strong>{{ analysis.role_identity.seniority }}</strong>
            </div>
            <div>
              <span>Requirement count</span>
              <strong>{{ analysis.required_capabilities.length }} capabilities</strong>
            </div>
          </div>
        </WorkspacePanel>

        <div class="metric-grid">
          <MetricBlock
            label="Technical requirements"
            :value="capabilityGroups.technical.length"
            detail="Tools, systems, methods"
          />
          <MetricBlock
            label="Business requirements"
            :value="capabilityGroups.business.length"
            detail="Domain, judgment, outcomes"
          />
          <MetricBlock
            label="Collaboration signals"
            :value="capabilityGroups.collaboration.length"
            detail="Stakeholder and team fit"
          />
          <MetricBlock
            label="Hidden expectations"
            :value="analysis.hidden_expectations.length"
            detail="Implicit hiring signals"
            variant="accent"
          />
        </div>

        <WorkspacePanel class="capability-section">
          <div class="section-heading">
            <span class="section-kicker">Core capabilities</span>
            <strong>{{ analysis.required_capabilities.length }}</strong>
          </div>
          <div class="capability-columns">
            <section
              v-for="group in groupedCapabilities"
              :key="group.label"
              class="capability-group"
            >
              <h3>{{ group.label }}</h3>
              <article
                v-for="capability in group.items"
                :key="capability.requirement_id"
                class="requirement-row"
              >
                <div class="card-topline">
                  <strong>{{ capability.name }}</strong>
                  <span>{{ capability.importance }}</span>
                </div>
                <p>{{ capability.evidence_signal }}</p>
                <div class="tag-row">
                  <span>{{ capability.category }}</span>
                  <span>{{ formatConfidence(capability.confidence) }}</span>
                </div>
              </article>
              <p v-if="!group.items.length" class="quiet-note">
                No explicit {{ group.label.toLowerCase() }} signal found in this JD.
              </p>
            </section>
          </div>
        </WorkspacePanel>

        <div class="role-detail-grid">
          <WorkspacePanel class="list-panel">
            <div class="section-heading">
              <span class="section-kicker">Hidden expectations</span>
              <strong>{{ analysis.hidden_expectations.length }}</strong>
            </div>
            <ol>
              <li v-for="item in analysis.hidden_expectations" :key="item">
                {{ item }}
              </li>
            </ol>
          </WorkspacePanel>

          <WorkspacePanel class="list-panel">
            <div class="section-heading">
              <span class="section-kicker">Work reality</span>
              <strong>{{ analysis.work_context.success_measures.length }}</strong>
            </div>
            <div class="work-context">
              <p>{{ analysis.work_context.environment }}</p>
              <p>{{ analysis.work_context.collaboration_model }}</p>
              <p>{{ analysis.work_context.pace }}</p>
            </div>
            <ol aria-label="Success measures">
              <li v-for="item in analysis.work_context.success_measures" :key="item">
                {{ item }}
              </li>
            </ol>
          </WorkspacePanel>
        </div>

        <WorkspacePanel class="list-panel responsibilities-panel">
          <div class="section-heading">
            <span class="section-kicker">Responsibilities</span>
            <strong>{{ analysis.responsibilities.length }}</strong>
          </div>
          <ol>
            <li v-for="item in analysis.responsibilities" :key="item">
              {{ item }}
            </li>
          </ol>
        </WorkspacePanel>
      </section>

      <section v-else-if="isAnalyzing" class="report-panel" aria-label="Role analysis progress">
        <WorkspacePanel class="loading-panel">
          <span class="section-kicker">Building role intelligence</span>
          <div class="skeleton skeleton-title" />
          <div class="skeleton skeleton-line" />
          <div class="skeleton skeleton-line short" />
        </WorkspacePanel>
        <div class="loading-grid">
          <div v-for="item in 4" :key="item" class="skeleton-card">
            <div class="skeleton skeleton-line short" />
            <div class="skeleton skeleton-title" />
            <div class="skeleton skeleton-line" />
          </div>
        </div>
      </section>

      <EmptyState
        v-else
        class="empty-report"
        eyebrow="Structured role intelligence"
        title="Analyze a JD to activate the role workspace"
        description="The report will prioritize role overview, core capabilities, hidden expectations, and practical work reality for downstream alignment analysis."
      />
    </div>
  </section>
</template>

<script setup lang="ts">
import { computed, onMounted, ref, watch } from "vue";
import { useRoute } from "vue-router";

import EmptyState from "../components/EmptyState.vue";
import MetricBlock from "../components/MetricBlock.vue";
import WorkspacePanel from "../components/WorkspacePanel.vue";
import {
  analyzeRole,
  getRoleTemplates,
  type RoleAnalysisResponse,
  type RoleCapabilityRequirement,
  type RoleTemplate
} from "../services/api";

const STORAGE_KEY = "careerlens.latestRoleRequirement";

const route = useRoute();
const inputMode = ref<"template" | "custom">("template");
const targetRole = ref("");
const jobDescription = ref("");
const selectedTemplateId = ref("");
const roleTemplates = ref<RoleTemplate[]>([]);
const analysis = ref<RoleAnalysisResponse | null>(loadSavedRole());
const isAnalyzing = ref(false);
const errorMessage = ref("");

const selectedTemplate = computed(
  () => roleTemplates.value.find((template) => template.template_id === selectedTemplateId.value) ?? null
);
const canAnalyze = computed(() =>
  inputMode.value === "template"
    ? Boolean(selectedTemplateId.value)
    : jobDescription.value.trim().length >= 20
);
const inputStatus = computed(() => {
  if (analysis.value) {
    return "Latest analysis saved";
  }

  if (inputMode.value === "template") {
    return selectedTemplate.value ? "Template ready" : "Choose a role template";
  }

  if (jobDescription.value.trim().length > 0 && !canAnalyze.value) {
    return "JD needs more detail";
  }

  return canAnalyze.value ? "Ready to analyze" : "Waiting for JD";
});

const capabilityGroups = computed(() => {
  const groups: Record<"technical" | "business" | "collaboration", RoleCapabilityRequirement[]> = {
    technical: [],
    business: [],
    collaboration: []
  };

  for (const capability of analysis.value?.required_capabilities ?? []) {
    const category = capability.category.toLowerCase();
    if (category.includes("technical") || category.includes("tool") || category.includes("data")) {
      groups.technical.push(capability);
    } else if (
      category.includes("collaboration") ||
      category.includes("communication") ||
      category.includes("stakeholder")
    ) {
      groups.collaboration.push(capability);
    } else {
      groups.business.push(capability);
    }
  }

  return groups;
});

const groupedCapabilities = computed(() => [
  { label: "Technical skills", items: capabilityGroups.value.technical },
  { label: "Business skills", items: capabilityGroups.value.business },
  { label: "Collaboration skills", items: capabilityGroups.value.collaboration }
]);

const handleAnalyze = async () => {
  if (!canAnalyze.value) {
    return;
  }

  isAnalyzing.value = true;
  errorMessage.value = "";

  try {
    analysis.value =
      inputMode.value === "template"
        ? await analyzeRole({ role_template_id: selectedTemplateId.value })
        : await analyzeRole({
            target_role: targetRole.value.trim() || undefined,
            job_description: jobDescription.value
          });
    localStorage.setItem(STORAGE_KEY, JSON.stringify(analysis.value));
  } catch {
    errorMessage.value = "Role analysis failed. Confirm the backend is running and try again.";
  } finally {
    isAnalyzing.value = false;
  }
};

function loadSavedRole(): RoleAnalysisResponse | null {
  const rawValue = localStorage.getItem(STORAGE_KEY);
  if (!rawValue) {
    return null;
  }

  try {
    return normalizeRoleAnalysis(JSON.parse(rawValue));
  } catch {
    return null;
  }
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
    source: role.source ?? "custom_jd",
    hidden_expectations: role.hidden_expectations ?? role.hidden_requirements ?? [],
    work_context: role.work_context ?? {
      environment: role.role_identity?.business_context ?? "Technology role context.",
      collaboration_model: "Cross-functional collaboration with stakeholders and delivery partners.",
      pace: "Moderate delivery cadence with discovery and execution cycles.",
      success_measures: role.responsibilities?.slice(0, 3) ?? []
    }
  };
}

const formatConfidence = (value: number): string => `${Math.round(value * 100)}%`;

onMounted(async () => {
  try {
    const response = await getRoleTemplates();
    roleTemplates.value = response.templates;
    const queryTemplateId = typeof route.query.template_id === "string" ? route.query.template_id : "";
    if (queryTemplateId && response.templates.some((template) => template.template_id === queryTemplateId)) {
      selectedTemplateId.value = queryTemplateId;
      inputMode.value = "template";
    }
  } catch {
    errorMessage.value = "Role templates failed to load. You can still paste a custom JD.";
    inputMode.value = "custom";
  }
});

watch(
  () => route.query.template_id,
  (templateId) => {
    if (typeof templateId === "string") {
      selectedTemplateId.value = templateId;
      inputMode.value = "template";
    }
  }
);
</script>

<style scoped>
.role-page,
.role-header {
  max-width: 1240px;
}

.role-workspace {
  display: grid;
  grid-template-columns: minmax(300px, 380px) minmax(0, 1fr);
  gap: 18px;
  align-items: start;
}

.input-panel {
  position: sticky;
  top: 24px;
  display: grid;
  gap: 18px;
  padding: 20px;
}

.input-panel form,
.panel-heading,
.report-panel,
.role-overview,
.capability-section,
.list-panel,
.loading-panel {
  display: grid;
  gap: 16px;
}

.panel-heading strong {
  color: var(--text);
  font-size: 15px;
}

.mode-switch {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 6px;
  border: 1px solid var(--border);
  border-radius: 8px;
  background: var(--surface-muted);
  padding: 4px;
}

.mode-switch button {
  min-height: 34px;
  border: 0;
  border-radius: 6px;
  background: transparent;
  color: var(--text-muted);
  cursor: pointer;
  font-size: 12px;
  font-weight: 760;
}

.mode-switch button.active {
  background: var(--surface);
  color: var(--text);
  box-shadow: var(--shadow-panel);
}

.template-preview {
  display: grid;
  gap: 10px;
  border: 1px solid var(--border);
  border-radius: 8px;
  background: var(--surface-subtle);
  padding: 14px;
}

.template-preview strong {
  color: var(--text);
  font-size: 15px;
}

.template-preview p {
  margin: 0;
  color: var(--text-muted);
  font-size: 13px;
  line-height: 1.5;
}

.role-overview,
.capability-section,
.list-panel,
.loading-panel {
  padding: 22px;
}

.role-overview__header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 16px;
}

.role-overview p,
.requirement-row p,
.work-context p,
.quiet-note,
.list-panel li {
  margin: 0;
  color: var(--text-muted);
  font-size: 14px;
  line-height: 1.55;
}

.role-overview > p {
  max-width: 78ch;
  font-size: 16px;
}

.identity-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 10px;
}

.identity-grid div {
  display: grid;
  gap: 5px;
  border: 1px solid var(--border);
  border-radius: 8px;
  background: var(--surface-subtle);
  padding: 12px;
}

.identity-grid span {
  color: var(--text-soft);
  font-size: 11px;
  font-weight: 760;
}

.identity-grid strong {
  color: var(--text);
  font-size: 13px;
  line-height: 1.35;
}

.capability-columns {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 12px;
}

.capability-group {
  display: grid;
  align-content: start;
  gap: 12px;
}

.requirement-row,
.skeleton-card {
  display: grid;
  gap: 12px;
  border: 1px solid var(--border);
  border-radius: 8px;
  background: var(--surface-subtle);
  padding: 14px;
}

.card-topline strong {
  color: var(--text);
  font-size: 14px;
  line-height: 1.35;
}

.role-detail-grid,
.loading-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 18px;
}

.list-panel {
  align-content: start;
}

.list-panel ol {
  display: grid;
  gap: 11px;
  margin: 0;
  padding-left: 20px;
}

.work-context {
  display: grid;
  gap: 9px;
  border-bottom: 1px solid var(--border);
  padding-bottom: 14px;
}

.responsibilities-panel {
  margin-top: 18px;
}

.list-panel li::marker {
  color: var(--text-soft);
  font-weight: 800;
  font-variant-numeric: tabular-nums;
}

.skeleton {
  overflow: hidden;
  border-radius: 8px;
  background: linear-gradient(90deg, #e8e4da 0%, #f5f3ed 48%, #e8e4da 100%);
  background-size: 220% 100%;
  animation: skeleton-pulse 1.5s ease-in-out infinite;
}

.skeleton-title {
  width: 62%;
  height: 28px;
}

.skeleton-line {
  width: 100%;
  height: 12px;
}

.skeleton-line.short {
  width: 46%;
}

@keyframes skeleton-pulse {
  from {
    background-position: 120% 0;
  }

  to {
    background-position: -120% 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .skeleton {
    animation: none;
  }
}

@media (max-width: 1120px) {
  .role-workspace,
  .capability-columns,
  .role-detail-grid,
  .identity-grid,
  .loading-grid {
    grid-template-columns: 1fr;
  }

  .input-panel {
    position: static;
  }
}
</style>

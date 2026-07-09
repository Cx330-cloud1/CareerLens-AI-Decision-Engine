<template>
  <section class="page-section optimization-page">
    <header class="page-header optimization-header">
      <div class="page-header__meta">
        <span class="status-token">Resume Optimization</span>
        <span :class="['status-token', canOptimize ? '' : 'status-token--neutral']">
          {{ canOptimize ? "Inputs ready" : "Needs resume and role" }}
        </span>
      </div>
      <h1>Turn fit gaps into resume positioning work</h1>
      <p class="lede">
        Convert current evidence, target role requirements, and alignment gaps into capability
        priorities, evidence upgrades, missing proof, and experience restructuring guidance.
      </p>
    </header>

    <div class="optimization-workspace">
      <aside class="control-rail">
        <WorkspacePanel class="input-panel">
          <div class="section-heading">
            <span class="section-kicker">Optimization inputs</span>
            <strong>{{ inputStatus }}</strong>
          </div>

          <div class="input-stack">
            <MetricBlock
              label="Current evidence"
              :value="resumeAnalysis?.experience_evidence.length ?? 0"
              detail="resume proof points"
              variant="muted"
            />
            <MetricBlock
              label="Role requirements"
              :value="roleRequirement?.required_capabilities.length ?? 0"
              detail="target capabilities"
              variant="muted"
            />
            <MetricBlock
              label="Capability gaps"
              :value="alignmentReport?.capability_gaps.length ?? 0"
              detail="from alignment report"
              :variant="alignmentReport?.capability_gaps.length ? 'danger' : 'muted'"
            />
          </div>

          <button class="primary-button" type="button" :disabled="isOptimizing || !canOptimize" @click="handleOptimize">
            {{ isOptimizing ? "Optimizing..." : "Generate optimization plan" }}
          </button>

          <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
        </WorkspacePanel>
      </aside>

      <main class="optimization-report">
        <template v-if="optimization">
          <section class="source-grid">
            <WorkspacePanel class="source-panel">
              <div class="section-heading">
                <span class="section-kicker">Current evidence</span>
                <strong>{{ resumeAnalysis?.experience_evidence.length ?? 0 }}</strong>
              </div>
              <article
                v-for="item in resumeAnalysis?.experience_evidence.slice(0, 4)"
                :key="item.evidence_id"
                class="source-row"
              >
                <span>{{ item.source_section }} / {{ item.strength }}</span>
                <p>{{ item.excerpt }}</p>
              </article>
            </WorkspacePanel>

            <WorkspacePanel class="source-panel">
              <div class="section-heading">
                <span class="section-kicker">Target role requirements</span>
                <strong>{{ roleRequirement?.required_capabilities.length ?? 0 }}</strong>
              </div>
              <article
                v-for="requirement in roleRequirement?.required_capabilities.slice(0, 4)"
                :key="requirement.requirement_id"
                class="source-row"
              >
                <span>{{ requirement.importance }} / {{ requirement.category }}</span>
                <p>{{ requirement.name }}: {{ requirement.evidence_signal }}</p>
              </article>
            </WorkspacePanel>
          </section>

          <section class="optimization-columns">
            <WorkspacePanel class="analysis-section">
              <div class="section-heading">
                <span class="section-kicker">Capability priorities</span>
                <strong>{{ optimization.capability_priorities.length }}</strong>
              </div>
              <article
                v-for="priority in optimization.capability_priorities"
                :key="priority.capability"
                class="optimization-card"
              >
                <div class="card-topline">
                  <h3>{{ priority.capability }}</h3>
                  <span>{{ priority.priority }}</span>
                </div>
                <p>{{ priority.reason }}</p>
                <div class="tag-row">
                  <span>{{ priority.category }}</span>
                  <span>{{ formatConfidence(priority.confidence) }}</span>
                </div>
              </article>
            </WorkspacePanel>

            <WorkspacePanel class="analysis-section">
              <div class="section-heading">
                <span class="section-kicker">Capability gaps</span>
                <strong>{{ optimization.missing_evidence.length }}</strong>
              </div>
              <article
                v-for="gap in optimization.missing_evidence"
                :key="gap.capability"
                class="optimization-card optimization-card--gap"
              >
                <div class="card-topline">
                  <h3>{{ gap.capability }}</h3>
                  <span>{{ gap.impact_level }}</span>
                </div>
                <p>{{ gap.evidence_needed }}</p>
                <small>{{ gap.suggested_proof }}</small>
              </article>
            </WorkspacePanel>
          </section>

          <WorkspacePanel class="analysis-section">
            <div class="section-heading">
              <span class="section-kicker">Improvement suggestions</span>
              <strong>{{ optimization.evidence_improvements.length }}</strong>
            </div>
            <article
              v-for="improvement in optimization.evidence_improvements"
              :key="improvement.evidence_id"
              class="evidence-upgrade"
            >
              <div>
                <span class="section-kicker">{{ improvement.capability }}</span>
                <h3>{{ improvement.improvement }}</h3>
                <p>{{ improvement.current_signal }}</p>
              </div>
              <strong>{{ improvement.quality_target }}</strong>
            </article>
          </WorkspacePanel>

          <WorkspacePanel class="analysis-section" variant="accent">
            <div class="section-heading">
              <span class="section-kicker">Experience restructuring guidance</span>
              <strong>{{ optimization.experience_reframing.length }}</strong>
            </div>
            <article
              v-for="reframe in optimization.experience_reframing"
              :key="`${reframe.source_section}-${reframe.target_capability}`"
              class="reframe-row"
            >
              <div class="card-topline">
                <h3>{{ reframe.target_capability }}</h3>
                <span>{{ reframe.source_section }}</span>
              </div>
              <p>{{ reframe.framing_guidance }}</p>
              <div class="reframe-grid">
                <div>
                  <span>Current signal</span>
                  <strong>{{ reframe.before_signal }}</strong>
                </div>
                <div>
                  <span>Target positioning</span>
                  <strong>{{ reframe.after_positioning }}</strong>
                </div>
              </div>
            </article>
          </WorkspacePanel>
        </template>

        <WorkspacePanel v-else class="empty-state">
          <span class="section-kicker">Optimization plan</span>
          <h2>Run Resume Intelligence and Role Intelligence first.</h2>
          <p>
            Alignment gaps are optional but recommended. When present, they prioritize missing
            evidence and make the optimization plan more targeted.
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
  optimizeResume,
  type AlignmentReport,
  type ResumeAnalysisResponse,
  type ResumeOptimization,
  type ResumeOptimizationResponse,
  type RoleAnalysisResponse,
  type RoleRequirement
} from "../services/api";

const ROLE_STORAGE_KEY = "careerlens.latestRoleRequirement";
const RESUME_STORAGE_KEY = "careerlens.latestResumeAnalysis";
const ALIGNMENT_STORAGE_KEY = "careerlens.latestAlignmentReport";
const OPTIMIZATION_STORAGE_KEY = "careerlens.latestResumeOptimization";

const resumeAnalysis = ref<ResumeAnalysisResponse | null>(loadStored<ResumeAnalysisResponse>(RESUME_STORAGE_KEY));
const roleRequirement = ref<RoleAnalysisResponse | null>(normalizeRoleAnalysis(loadStored<RoleAnalysisResponse>(ROLE_STORAGE_KEY)));
const alignmentReport = ref<AlignmentReport | null>(loadStored<AlignmentReport>(ALIGNMENT_STORAGE_KEY));
const optimizationResponse = ref<ResumeOptimizationResponse | null>(
  loadStored<ResumeOptimizationResponse>(OPTIMIZATION_STORAGE_KEY)
);
const isOptimizing = ref(false);
const errorMessage = ref("");

const optimization = computed<ResumeOptimization | null>(
  () => optimizationResponse.value?.resume_optimization ?? null
);
const canOptimize = computed(() => Boolean(resumeAnalysis.value && roleRequirement.value));
const inputStatus = computed(() => {
  if (!resumeAnalysis.value && !roleRequirement.value) {
    return "Resume and role missing";
  }
  if (!resumeAnalysis.value) {
    return "Resume missing";
  }
  if (!roleRequirement.value) {
    return "Role missing";
  }
  return alignmentReport.value ? "Full context ready" : "Base context ready";
});

const handleOptimize = async () => {
  if (!resumeAnalysis.value || !roleRequirement.value) {
    return;
  }

  isOptimizing.value = true;
  errorMessage.value = "";

  try {
    optimizationResponse.value = await optimizeResume({
      resume_evidence: resumeAnalysis.value.experience_evidence,
      target_role: toRoleRequirement(roleRequirement.value),
      alignment_gaps: alignmentReport.value?.capability_gaps ?? [],
      alignment_report: alignmentReport.value
    });
    localStorage.setItem(OPTIMIZATION_STORAGE_KEY, JSON.stringify(optimizationResponse.value));
  } catch {
    errorMessage.value = "Resume optimization failed. Confirm the backend is running and try again.";
  } finally {
    isOptimizing.value = false;
  }
};

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

function normalizeRoleAnalysis(role: RoleAnalysisResponse | null): RoleAnalysisResponse | null {
  if (!role) {
    return null;
  }

  return {
    ...role,
    hidden_expectations: role.hidden_expectations ?? [],
    work_context: role.work_context ?? {
      environment: role.role_identity?.business_context ?? "Technology role context.",
      collaboration_model: "Cross-functional collaboration with stakeholders and delivery partners.",
      pace: "Moderate delivery cadence with discovery and execution cycles.",
      success_measures: role.responsibilities?.slice(0, 3) ?? []
    }
  };
}

const formatConfidence = (value: number): string => `${Math.round(value * 100)}%`;
</script>

<style scoped>
.optimization-page,
.optimization-header {
  max-width: 1240px;
}

.optimization-workspace {
  display: grid;
  grid-template-columns: minmax(280px, 340px) minmax(0, 1fr);
  gap: 18px;
  align-items: start;
}

.control-rail {
  position: sticky;
  top: 18px;
}

.input-panel,
.analysis-section,
.source-panel {
  display: grid;
  gap: 14px;
  padding: 18px;
}

.input-stack,
.optimization-report {
  display: grid;
  gap: 14px;
}

.source-grid,
.optimization-columns {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 14px;
}

.source-row,
.optimization-card,
.evidence-upgrade,
.reframe-row {
  display: grid;
  gap: 10px;
  border-top: 1px solid var(--border);
  padding-top: 12px;
}

.source-row span,
.reframe-grid span {
  color: var(--text-soft);
  font-size: 11px;
  font-weight: 760;
  text-transform: uppercase;
}

.source-row p,
.optimization-card p,
.optimization-card small,
.evidence-upgrade p,
.reframe-row p {
  margin: 0;
  color: var(--text-muted);
  font-size: 14px;
  line-height: 1.55;
}

.optimization-card--gap .card-topline span {
  background: var(--surface-danger);
  color: var(--danger);
}

.evidence-upgrade {
  grid-template-columns: minmax(0, 1.4fr) minmax(220px, 0.7fr);
  align-items: start;
}

.evidence-upgrade strong {
  border-radius: 8px;
  background: var(--surface-subtle);
  color: var(--text);
  font-size: 13px;
  font-weight: 700;
  line-height: 1.45;
  padding: 12px;
}

.reframe-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 10px;
}

.reframe-grid div {
  display: grid;
  gap: 6px;
  border: 1px solid var(--border);
  border-radius: 8px;
  background: rgb(255 254 250 / 70%);
  padding: 12px;
}

.reframe-grid strong {
  color: var(--text);
  font-size: 13px;
  font-weight: 650;
  line-height: 1.45;
}

@media (max-width: 1080px) {
  .optimization-workspace,
  .source-grid,
  .optimization-columns,
  .evidence-upgrade,
  .reframe-grid {
    grid-template-columns: 1fr;
  }

  .control-rail {
    position: static;
  }
}
</style>

<template>
  <section class="page-section strategy-page">
    <header class="page-header strategy-header">
      <div class="page-header__meta">
        <span class="status-token">Career Strategy</span>
        <span :class="['status-token', canGenerate ? '' : 'status-token--neutral']">
          {{ canGenerate ? "Optimization ready" : "Needs optimization" }}
        </span>
      </div>
      <h1>Build an evidence-backed development roadmap</h1>
      <p class="lede">
        Turn resume optimization work into prioritized actions, capability development, and
        recommended proof-building projects for the selected target role.
      </p>
    </header>

    <div class="strategy-workspace">
      <aside class="control-rail">
        <WorkspacePanel class="input-panel">
          <div class="section-heading">
            <span class="section-kicker">Strategy source</span>
            <strong>{{ inputStatus }}</strong>
          </div>
          <MetricBlock
            label="Capability priorities"
            :value="optimization?.capability_priorities.length ?? 0"
            detail="from resume optimization"
            variant="muted"
          />
          <MetricBlock
            label="Missing evidence"
            :value="optimization?.missing_evidence.length ?? 0"
            detail="proof to create"
            :variant="optimization?.missing_evidence.length ? 'danger' : 'muted'"
          />
          <button class="primary-button" type="button" :disabled="isGenerating || !canGenerate" @click="handleGenerate">
            {{ isGenerating ? "Generating..." : "Generate career strategy" }}
          </button>
          <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
        </WorkspacePanel>
      </aside>

      <main class="strategy-report">
        <template v-if="careerPlan">
          <section class="overview-grid">
            <MetricBlock
              label="Short-term actions"
              :value="careerPlan.short_term_actions.length"
              detail="resume and evidence upgrades"
            />
            <MetricBlock
              label="Medium-term actions"
              :value="careerPlan.medium_term_actions.length"
              detail="capability development"
            />
            <MetricBlock
              label="Recommended projects"
              :value="careerPlan.recommended_projects.length"
              detail="evidence builders"
              variant="accent"
            />
            <MetricBlock
              label="Growth path"
              :value="careerPlan.capability_growth_path.length"
              detail="validation steps"
            />
          </section>

          <section class="action-columns">
            <WorkspacePanel class="strategy-section">
              <div class="section-heading">
                <span class="section-kicker">Prioritized actions</span>
                <strong>{{ careerPlan.short_term_actions.length }}</strong>
              </div>
              <article
                v-for="action in careerPlan.short_term_actions"
                :key="action.title"
                class="action-card"
              >
                <div class="card-topline">
                  <h3>{{ action.title }}</h3>
                  <span>{{ action.priority }}</span>
                </div>
                <p>{{ action.rationale }}</p>
                <small>{{ action.evidence_outcome }}</small>
              </article>
            </WorkspacePanel>

            <WorkspacePanel class="strategy-section">
              <div class="section-heading">
                <span class="section-kicker">Development roadmap</span>
                <strong>{{ careerPlan.medium_term_actions.length }}</strong>
              </div>
              <article
                v-for="action in careerPlan.medium_term_actions"
                :key="action.title"
                class="action-card"
              >
                <div class="card-topline">
                  <h3>{{ action.title }}</h3>
                  <span>{{ action.priority }}</span>
                </div>
                <p>{{ action.rationale }}</p>
                <small>{{ action.evidence_outcome }}</small>
              </article>
            </WorkspacePanel>
          </section>

          <WorkspacePanel class="strategy-section" variant="accent">
            <div class="section-heading">
              <span class="section-kicker">Recommended evidence building</span>
              <strong>{{ careerPlan.recommended_projects.length }}</strong>
            </div>
            <div class="project-grid">
              <article
                v-for="project in careerPlan.recommended_projects"
                :key="project.title"
                class="project-card"
              >
                <h3>{{ project.title }}</h3>
                <p>{{ project.scope }}</p>
                <small>{{ project.evidence_to_create }}</small>
                <div class="tag-row">
                  <span v-for="capability in project.target_capabilities" :key="capability">
                    {{ capability }}
                  </span>
                </div>
              </article>
            </div>
          </WorkspacePanel>

          <WorkspacePanel class="strategy-section">
            <div class="section-heading">
              <span class="section-kicker">Capability growth path</span>
              <strong>{{ careerPlan.capability_growth_path.length }}</strong>
            </div>
            <article
              v-for="step in careerPlan.capability_growth_path"
              :key="step.capability"
              class="growth-row"
            >
              <h3>{{ step.capability }}</h3>
              <div class="growth-grid">
                <div>
                  <span>Current gap</span>
                  <p>{{ step.current_gap }}</p>
                </div>
                <div>
                  <span>Next signal</span>
                  <p>{{ step.next_level_signal }}</p>
                </div>
                <div>
                  <span>Validation</span>
                  <p>{{ step.validation_method }}</p>
                </div>
              </div>
            </article>
          </WorkspacePanel>
        </template>

        <WorkspacePanel v-else class="empty-state">
          <span class="section-kicker">Career plan</span>
          <h2>Generate resume optimization before career strategy.</h2>
          <p>
            This plan uses capability priorities and missing evidence from Resume Optimization,
            then turns them into actions and proof-building projects.
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
  generateCareerStrategy,
  type AlignmentReport,
  type CareerPlan,
  type CareerStrategyResponse,
  type ResumeOptimization,
  type ResumeOptimizationResponse,
  type RoleAnalysisResponse,
  type RoleRequirement
} from "../services/api";

const ROLE_STORAGE_KEY = "careerlens.latestRoleRequirement";
const ALIGNMENT_STORAGE_KEY = "careerlens.latestAlignmentReport";
const OPTIMIZATION_STORAGE_KEY = "careerlens.latestResumeOptimization";
const CAREER_STRATEGY_STORAGE_KEY = "careerlens.latestCareerStrategy";

const roleRequirement = ref<RoleAnalysisResponse | null>(normalizeRoleAnalysis(loadStored<RoleAnalysisResponse>(ROLE_STORAGE_KEY)));
const alignmentReport = ref<AlignmentReport | null>(loadStored<AlignmentReport>(ALIGNMENT_STORAGE_KEY));
const optimizationResponse = ref<ResumeOptimizationResponse | null>(
  loadStored<ResumeOptimizationResponse>(OPTIMIZATION_STORAGE_KEY)
);
const strategyResponse = ref<CareerStrategyResponse | null>(
  loadStored<CareerStrategyResponse>(CAREER_STRATEGY_STORAGE_KEY)
);
const isGenerating = ref(false);
const errorMessage = ref("");

const optimization = computed<ResumeOptimization | null>(
  () => optimizationResponse.value?.resume_optimization ?? null
);
const careerPlan = computed<CareerPlan | null>(() => strategyResponse.value?.career_plan ?? null);
const canGenerate = computed(() => Boolean(optimization.value && roleRequirement.value));
const inputStatus = computed(() => {
  if (!optimization.value && !roleRequirement.value) {
    return "Optimization and role missing";
  }
  if (!optimization.value) {
    return "Optimization missing";
  }
  if (!roleRequirement.value) {
    return "Role missing";
  }
  return "Ready";
});

const handleGenerate = async () => {
  if (!optimization.value || !roleRequirement.value) {
    return;
  }

  isGenerating.value = true;
  errorMessage.value = "";

  try {
    strategyResponse.value = await generateCareerStrategy({
      resume_optimization: optimization.value,
      target_role: toRoleRequirement(roleRequirement.value),
      alignment_report: alignmentReport.value
    });
    localStorage.setItem(CAREER_STRATEGY_STORAGE_KEY, JSON.stringify(strategyResponse.value));
  } catch {
    errorMessage.value = "Career strategy generation failed. Confirm the backend is running and try again.";
  } finally {
    isGenerating.value = false;
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
</script>

<style scoped>
.strategy-page,
.strategy-header {
  max-width: 1240px;
}

.strategy-workspace {
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
.strategy-section {
  display: grid;
  gap: 14px;
  padding: 18px;
}

.strategy-report,
.action-columns {
  display: grid;
  gap: 14px;
}

.overview-grid,
.action-columns,
.project-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 14px;
}

.overview-grid {
  grid-template-columns: repeat(4, minmax(0, 1fr));
}

.action-card,
.project-card,
.growth-row {
  display: grid;
  gap: 10px;
  border-top: 1px solid var(--border);
  padding-top: 12px;
}

.action-card p,
.action-card small,
.project-card p,
.project-card small,
.growth-grid p {
  margin: 0;
  color: var(--text-muted);
  font-size: 14px;
  line-height: 1.55;
}

.project-card {
  border: 1px solid var(--border);
  border-radius: 8px;
  background: rgb(255 254 250 / 70%);
  padding: 14px;
}

.growth-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 10px;
}

.growth-grid div {
  display: grid;
  gap: 6px;
  border: 1px solid var(--border);
  border-radius: 8px;
  background: var(--surface-subtle);
  padding: 12px;
}

.growth-grid span {
  color: var(--text-soft);
  font-size: 11px;
  font-weight: 760;
  text-transform: uppercase;
}

@media (max-width: 1080px) {
  .strategy-workspace,
  .overview-grid,
  .action-columns,
  .project-grid,
  .growth-grid {
    grid-template-columns: 1fr;
  }

  .control-rail {
    position: static;
  }
}
</style>

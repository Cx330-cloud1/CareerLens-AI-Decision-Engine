<template>
  <section class="page-section resume-intelligence">
    <header class="page-header profile-header">
      <div class="page-header__meta">
        <span class="status-token">Resume Intelligence</span>
        <span :class="['status-token', analysis ? '' : 'status-token--neutral']">
          {{ analysis ? "Analysis ready" : "Awaiting input" }}
        </span>
      </div>
      <h1>Build a professional talent dossier</h1>
      <p class="lede">
        Upload a resume or paste text to produce structured candidate identity, capability
        signals, evidence strength, confidence, and improvement priorities.
      </p>
    </header>

    <div class="intelligence-workspace">
      <WorkspacePanel class="upload-panel">
        <div class="panel-heading">
          <span class="section-kicker">Candidate input</span>
          <strong>{{ uploadStatus }}</strong>
        </div>

        <form @submit.prevent="handleAnalyze">
          <label class="upload-dropzone">
            <span class="upload-title">{{ t("pages.talentProfile.upload.title") }}</span>
            <span class="upload-copy">
              {{ selectedFileName || t("pages.talentProfile.upload.description") }}
            </span>
            <input
              type="file"
              accept=".pdf,.txt,.md,.doc,.docx"
              @change="handleFileChange"
            />
          </label>

          <label class="field-group">
            <span>{{ t("pages.talentProfile.fields.resumeText.label") }}</span>
            <textarea
              v-model="resumeText"
              :placeholder="t('pages.talentProfile.fields.resumeText.placeholder')"
              rows="12"
            />
          </label>

          <button class="primary-button" type="submit" :disabled="isAnalyzing || !canAnalyze">
            {{ isAnalyzing ? t("pages.talentProfile.actions.analyzing") : t("pages.talentProfile.actions.analyze") }}
          </button>

          <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
        </form>
      </WorkspacePanel>

      <section
        v-if="analysis"
        class="analysis-panel"
        :aria-label="t('pages.talentProfile.report.ariaLabel')"
      >
        <WorkspacePanel class="identity-card">
          <div class="identity-card__header">
            <div>
              <span class="section-kicker">{{ t("pages.talentProfile.report.candidateIdentity") }}</span>
              <h2>{{ analysis.candidate_identity.headline }}</h2>
            </div>
            <span class="confidence-badge">
              {{ formatConfidence(analysis.candidate_identity.confidence) }}
            </span>
          </div>
          <p>{{ analysis.candidate_identity.summary }}</p>
          <div class="identity-meta">
            <div>
              <span>Name</span>
              <strong>{{ analysis.candidate_identity.name || "Unknown" }}</strong>
            </div>
            <div>
              <span>Target direction</span>
              <strong>{{ analysis.candidate_identity.target_direction || "Not specified" }}</strong>
            </div>
            <div>
              <span>Parsing status</span>
              <strong>{{ analysis.parsing_status }}</strong>
            </div>
          </div>
          <ConfidenceMeter
            :value="analysis.candidate_identity.confidence"
            label="Identity confidence"
          />
        </WorkspacePanel>

        <div class="metric-grid">
          <MetricBlock
            label="Capability signals"
            :value="analysis.capabilities.length"
            detail="Mapped from resume evidence"
          />
          <MetricBlock
            label="Evidence cards"
            :value="analysis.experience_evidence.length"
            detail="Source excerpts extracted"
          />
          <MetricBlock
            label="Improvement priorities"
            :value="analysis.improvement_suggestions.length"
            detail="Ordered by career impact"
          />
          <MetricBlock
            label="Average confidence"
            :value="averageConfidence"
            detail="Across capability map"
            variant="accent"
          />
        </div>

        <WorkspacePanel class="capability-map">
          <div class="section-heading">
            <span class="section-kicker">Capability map</span>
            <strong>{{ analysis.capabilities.length }}</strong>
          </div>
          <div class="capability-grid">
            <article
              v-for="capability in analysis.capabilities"
              :key="capability.capability_id"
              class="capability-card"
            >
              <div class="card-topline">
                <h3>{{ capability.name }}</h3>
                <span>{{ capability.level }}</span>
              </div>
              <p>{{ capability.rationale }}</p>
              <div class="tag-row">
                <span>{{ capability.category }}</span>
                <span>{{ capability.evidence_ids.length }} evidence links</span>
              </div>
              <ConfidenceMeter :value="capability.confidence" label="Capability confidence" />
            </article>
          </div>
        </WorkspacePanel>

        <div class="evidence-layout">
          <WorkspacePanel class="evidence-panel">
            <div class="section-heading">
              <span class="section-kicker">Experience evidence</span>
              <strong>{{ analysis.experience_evidence.length }}</strong>
            </div>
            <EvidenceCard
              v-for="item in analysis.experience_evidence"
              :key="item.evidence_id"
              :source="item.source_section"
              :strength="item.strength"
              :excerpt="item.excerpt"
              :confidence="item.confidence"
              :capability="evidenceCapabilityMap[item.evidence_id]?.capability"
              :relevance="evidenceCapabilityMap[item.evidence_id]?.relevance"
            />
          </WorkspacePanel>

          <WorkspacePanel class="suggestion-panel">
            <div class="section-heading">
              <span class="section-kicker">Improvement queue</span>
              <strong>{{ analysis.improvement_suggestions.length }}</strong>
            </div>
            <article
              v-for="suggestion in analysis.improvement_suggestions"
              :key="suggestion.suggestion_id"
              class="suggestion-card"
            >
              <div class="card-topline">
                <h3>{{ suggestion.title }}</h3>
                <span>{{ suggestion.priority }}</span>
              </div>
              <p>{{ suggestion.rationale }}</p>
              <ConfidenceMeter :value="suggestion.confidence" label="Recommendation confidence" />
            </article>
          </WorkspacePanel>
        </div>
      </section>

      <section
        v-else-if="isAnalyzing"
        class="analysis-panel"
        :aria-label="t('pages.talentProfile.report.ariaLabel')"
      >
        <WorkspacePanel class="loading-panel">
          <span class="section-kicker">Analyzing evidence</span>
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
        :aria-label="t('pages.talentProfile.empty.ariaLabel')"
        :eyebrow="t('pages.talentProfile.empty.title')"
        title="A structured report will appear here"
        :description="t('pages.talentProfile.empty.description')"
      />
    </div>
  </section>
</template>

<script setup lang="ts">
import { computed, ref } from "vue";
import { useI18n } from "vue-i18n";

import ConfidenceMeter from "../components/ConfidenceMeter.vue";
import EmptyState from "../components/EmptyState.vue";
import EvidenceCard from "../components/EvidenceCard.vue";
import MetricBlock from "../components/MetricBlock.vue";
import WorkspacePanel from "../components/WorkspacePanel.vue";
import { analyzeResume, type ResumeAnalysisResponse } from "../services/api";

const RESUME_STORAGE_KEY = "careerlens.latestResumeAnalysis";

const { t } = useI18n();

const selectedFile = ref<File | null>(null);
const selectedFileName = ref("");
const resumeText = ref("");
const analysis = ref<ResumeAnalysisResponse | null>(loadSavedResume());
const isAnalyzing = ref(false);
const errorMessage = ref("");

const canAnalyze = computed(() => Boolean(selectedFile.value || resumeText.value.trim()));
const uploadStatus = computed(() => {
  if (!selectedFile.value && !resumeText.value.trim()) {
    return t("pages.talentProfile.upload.emptyStatus");
  }

  if (selectedFile.value) {
    return t("pages.talentProfile.upload.readyStatus", {
      name: selectedFile.value.name
    });
  }

  return t("pages.talentProfile.upload.textReadyStatus");
});

const averageConfidence = computed(() => {
  const capabilities = analysis.value?.capabilities ?? [];
  if (!capabilities.length) {
    return "Pending";
  }

  const total = capabilities.reduce((sum, capability) => sum + capability.confidence, 0);
  return `${Math.round((total / capabilities.length) * 100)}%`;
});

const evidenceCapabilityMap = computed(() => {
  const result: Record<string, { capability: string; relevance: string }> = {};

  for (const capability of analysis.value?.capabilities ?? []) {
    for (const evidenceId of capability.evidence_ids) {
      result[evidenceId] = {
        capability: capability.name,
        relevance: `${capability.category} signal at ${capability.level} level`
      };
    }
  }

  return result;
});

const handleFileChange = async (event: Event) => {
  const input = event.target as HTMLInputElement;
  const file = input.files?.[0] ?? null;
  selectedFile.value = file;
  selectedFileName.value = file?.name ?? "";
  errorMessage.value = "";

  if (!file) {
    return;
  }

  if (isTextReadable(file)) {
    resumeText.value = await file.text();
  }
};

const handleAnalyze = async () => {
  if (!canAnalyze.value) {
    return;
  }

  isAnalyzing.value = true;
  errorMessage.value = "";

  try {
    analysis.value = await analyzeResume({
      file_name: selectedFile.value?.name ?? "pasted-resume.txt",
      content_type: selectedFile.value?.type,
      file_size: selectedFile.value?.size ?? resumeText.value.length,
      resume_text: resumeText.value
    });
    localStorage.setItem(RESUME_STORAGE_KEY, JSON.stringify(analysis.value));
  } catch {
    errorMessage.value = t("pages.talentProfile.errors.analysisFailed");
  } finally {
    isAnalyzing.value = false;
  }
};

const isTextReadable = (file: File): boolean => {
  return (
    file.type.startsWith("text/") ||
    file.name.endsWith(".txt") ||
    file.name.endsWith(".md")
  );
};

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

const formatConfidence = (value: number): string => `${Math.round(value * 100)}%`;
</script>

<style scoped>
.resume-intelligence {
  display: grid;
  gap: 24px;
}

.profile-header {
  max-width: 940px;
}

.intelligence-workspace {
  display: grid;
  grid-template-columns: minmax(300px, 390px) minmax(0, 1fr);
  gap: 18px;
  align-items: start;
}

.upload-panel {
  position: sticky;
  top: 24px;
  display: grid;
  gap: 18px;
  padding: 20px;
}

.panel-heading {
  display: grid;
  gap: 6px;
}

.panel-heading strong {
  color: var(--text);
  font-size: 15px;
}

.upload-panel form {
  display: grid;
  gap: 16px;
}

.upload-dropzone {
  position: relative;
  display: grid;
  gap: 8px;
  min-height: 154px;
  align-content: center;
  border: 1px dashed var(--border-strong);
  border-radius: 10px;
  background: #f5f3ed;
  color: #4d504b;
  cursor: pointer;
  padding: 22px;
}

.upload-dropzone:hover {
  border-color: #9ea997;
  background: #f0eee8;
}

.upload-dropzone input {
  position: absolute;
  inset: 0;
  cursor: pointer;
  opacity: 0;
}

.upload-title {
  color: var(--text);
  font-size: 16px;
  font-weight: 780;
}

.upload-copy {
  color: var(--text-muted);
  font-size: 13px;
  line-height: 1.5;
}

.analysis-panel {
  display: grid;
  gap: 18px;
}

.identity-card,
.capability-map,
.evidence-panel,
.suggestion-panel,
.loading-panel {
  display: grid;
  gap: 18px;
  padding: 22px;
}

.identity-card__header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 16px;
}

.identity-card p,
.capability-card p,
.suggestion-card p {
  margin: 0;
  color: var(--text-muted);
  font-size: 14px;
  line-height: 1.6;
}

.identity-card > p {
  max-width: 78ch;
  font-size: 16px;
}

.identity-meta {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 10px;
}

.identity-meta div {
  display: grid;
  gap: 5px;
  border: 1px solid var(--border);
  border-radius: 10px;
  background: #fbfaf7;
  padding: 12px;
}

.identity-meta span {
  color: var(--text-soft);
  font-size: 11px;
  font-weight: 760;
}

.identity-meta strong {
  color: var(--text);
  font-size: 13px;
  line-height: 1.35;
}

.capability-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 12px;
}

.capability-card,
.suggestion-card,
.skeleton-card {
  display: grid;
  gap: 14px;
  border: 1px solid var(--border);
  border-radius: 10px;
  background: #fffefa;
  padding: 16px;
}

.evidence-layout {
  display: grid;
  grid-template-columns: 1.08fr 0.92fr;
  gap: 18px;
}

.evidence-panel,
.suggestion-panel {
  align-content: start;
}

.loading-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 12px;
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

@media (max-width: 1100px) {
  .intelligence-workspace,
  .capability-grid,
  .evidence-layout,
  .identity-meta,
  .loading-grid {
    grid-template-columns: 1fr;
  }

  .upload-panel {
    position: static;
  }
}
</style>

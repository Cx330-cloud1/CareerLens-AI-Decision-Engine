<template>
  <section class="page-section resume-intelligence">
    <header class="profile-header">
      <p class="eyebrow">{{ t("pages.talentProfile.eyebrow") }}</p>
      <h1>{{ t("pages.talentProfile.title") }}</h1>
      <p class="lede">{{ t("pages.talentProfile.lede") }}</p>
    </header>

    <div class="intelligence-workspace">
      <form class="upload-panel" @submit.prevent="handleAnalyze">
        <label class="upload-dropzone">
          <span class="upload-title">{{ t("pages.talentProfile.upload.title") }}</span>
          <span class="upload-copy">{{ selectedFileName || t("pages.talentProfile.upload.description") }}</span>
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
            rows="10"
          />
        </label>

        <div class="upload-meta">
          <span>{{ t("pages.talentProfile.upload.status") }}</span>
          <strong>{{ uploadStatus }}</strong>
        </div>

        <button class="analyze-button" type="submit" :disabled="isAnalyzing || !canAnalyze">
          {{ isAnalyzing ? t("pages.talentProfile.actions.analyzing") : t("pages.talentProfile.actions.analyze") }}
        </button>

        <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
      </form>

      <section
        v-if="analysis"
        class="analysis-panel"
        :aria-label="t('pages.talentProfile.report.ariaLabel')"
      >
        <article class="identity-card">
          <div>
            <span class="card-label">{{ t("pages.talentProfile.report.candidateIdentity") }}</span>
            <h2>{{ analysis.candidate_identity.headline }}</h2>
          </div>
          <span class="confidence-badge">
            {{ formatConfidence(analysis.candidate_identity.confidence) }}
          </span>
          <p>{{ analysis.candidate_identity.summary }}</p>
        </article>

        <div class="section-heading">
          <span class="card-label">{{ t("pages.talentProfile.report.capabilities") }}</span>
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
              <span>{{ formatConfidence(capability.confidence) }}</span>
            </div>
            <p>{{ capability.rationale }}</p>
            <div class="tag-row">
              <span>{{ capability.category }}</span>
              <span>{{ capability.level }}</span>
            </div>
          </article>
        </div>

        <div class="evidence-layout">
          <section class="evidence-panel">
            <div class="section-heading">
              <span class="card-label">{{ t("pages.talentProfile.report.evidence") }}</span>
              <strong>{{ analysis.experience_evidence.length }}</strong>
            </div>
            <article
              v-for="item in analysis.experience_evidence"
              :key="item.evidence_id"
              class="evidence-card"
            >
              <div class="card-topline">
                <span>{{ item.source_section }}</span>
                <strong>{{ item.strength }}</strong>
              </div>
              <p>{{ item.excerpt }}</p>
            </article>
          </section>

          <section class="suggestion-panel">
            <div class="section-heading">
              <span class="card-label">{{ t("pages.talentProfile.report.suggestions") }}</span>
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
            </article>
          </section>
        </div>
      </section>

      <section v-else class="empty-report" :aria-label="t('pages.talentProfile.empty.ariaLabel')">
        <span class="card-label">{{ t("pages.talentProfile.empty.title") }}</span>
        <p>{{ t("pages.talentProfile.empty.description") }}</p>
      </section>
    </div>
  </section>
</template>

<script setup lang="ts">
import { computed, ref } from "vue";
import { useI18n } from "vue-i18n";

import { analyzeResume, type ResumeAnalysisResponse } from "../services/api";

const { t } = useI18n();

const selectedFile = ref<File | null>(null);
const selectedFileName = ref("");
const resumeText = ref("");
const analysis = ref<ResumeAnalysisResponse | null>(null);
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

const formatConfidence = (value: number): string => `${Math.round(value * 100)}%`;
</script>

<style scoped>
.resume-intelligence {
  max-width: 1180px;
}

.profile-header {
  margin-bottom: 28px;
}

.intelligence-workspace {
  display: grid;
  grid-template-columns: minmax(300px, 400px) 1fr;
  gap: 24px;
  align-items: start;
}

.upload-panel,
.empty-report,
.identity-card,
.capability-card,
.evidence-card,
.suggestion-card {
  border: 1px solid #dedbd2;
  border-radius: 8px;
  background: #fff;
  box-shadow: 0 1px 2px rgb(17 24 39 / 5%);
}

.upload-panel {
  display: grid;
  gap: 18px;
  padding: 20px;
}

.upload-dropzone {
  position: relative;
  display: grid;
  gap: 8px;
  min-height: 148px;
  align-content: center;
  border: 1px dashed #9ca3af;
  border-radius: 8px;
  background: #fafafa;
  color: #374151;
  cursor: pointer;
  padding: 22px;
}

.upload-dropzone input {
  position: absolute;
  inset: 0;
  cursor: pointer;
  opacity: 0;
}

.upload-title {
  color: #111827;
  font-size: 16px;
  font-weight: 750;
}

.upload-copy,
.upload-meta {
  color: #6b7280;
  font-size: 13px;
  line-height: 1.45;
}

.field-group {
  display: grid;
  gap: 8px;
  color: #374151;
  font-size: 14px;
  font-weight: 650;
}

.field-group textarea {
  width: 100%;
  resize: vertical;
  border: 1px solid #d1d5db;
  border-radius: 8px;
  color: #111827;
  font: inherit;
  font-size: 14px;
  line-height: 1.5;
  padding: 10px 12px;
}

.field-group textarea:focus {
  outline: 2px solid #2563eb;
  outline-offset: 1px;
  border-color: #2563eb;
}

.upload-meta {
  display: flex;
  justify-content: space-between;
  gap: 12px;
}

.upload-meta strong {
  color: #111827;
  font-weight: 650;
  text-align: right;
}

.analyze-button {
  border: 0;
  border-radius: 8px;
  background: #111827;
  color: #fff;
  cursor: pointer;
  font: inherit;
  font-weight: 700;
  padding: 12px 16px;
}

.analyze-button:disabled {
  cursor: not-allowed;
  opacity: 0.55;
}

.error-message {
  margin: 0;
  color: #b91c1c;
  font-size: 14px;
  line-height: 1.5;
}

.analysis-panel {
  display: grid;
  gap: 18px;
}

.identity-card,
.capability-card,
.evidence-card,
.suggestion-card,
.empty-report {
  padding: 20px;
}

.identity-card {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 12px;
}

.identity-card p {
  grid-column: 1 / -1;
  margin: 0;
  color: #374151;
  font-size: 16px;
  line-height: 1.65;
}

h2,
h3 {
  margin: 0;
  color: #111827;
}

h2 {
  margin-top: 6px;
  font-size: 22px;
}

h3 {
  font-size: 15px;
  line-height: 1.35;
}

.card-label {
  color: #6b7280;
  font-size: 12px;
  font-weight: 750;
  letter-spacing: 0;
  text-transform: uppercase;
}

.confidence-badge,
.tag-row span,
.card-topline span,
.card-topline strong {
  border-radius: 999px;
  background: #eef2ff;
  color: #3730a3;
  font-size: 12px;
  font-weight: 750;
  line-height: 1;
  padding: 7px 9px;
  white-space: nowrap;
}

.section-heading,
.card-topline {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}

.section-heading strong {
  color: #111827;
  font-size: 14px;
}

.capability-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 14px;
}

.capability-card,
.evidence-card,
.suggestion-card {
  display: grid;
  gap: 12px;
}

.capability-card p,
.evidence-card p,
.suggestion-card p,
.empty-report p {
  margin: 0;
  color: #4b5563;
  font-size: 14px;
  line-height: 1.55;
}

.tag-row {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.tag-row span {
  background: #f3f4f6;
  color: #374151;
}

.evidence-layout {
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: 18px;
}

.evidence-panel,
.suggestion-panel {
  display: grid;
  gap: 12px;
  align-content: start;
}

.empty-report {
  min-height: 280px;
}

@media (max-width: 1040px) {
  .intelligence-workspace,
  .evidence-layout,
  .capability-grid {
    grid-template-columns: 1fr;
  }
}
</style>

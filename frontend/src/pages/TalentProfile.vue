<template>
  <section class="page-section talent-profile">
    <header class="profile-header">
      <p class="eyebrow">{{ t("pages.talentProfile.eyebrow") }}</p>
      <h1>{{ t("pages.talentProfile.title") }}</h1>
      <p class="lede">{{ t("pages.talentProfile.lede") }}</p>
    </header>

    <div class="profile-workspace">
      <form class="profile-form" @submit.prevent="handleAnalyze">
        <label v-for="field in fields" :key="field.key" class="field-group">
          <span>{{ t(field.labelKey) }}</span>
          <textarea
            v-model="form[field.key]"
            :placeholder="t(field.placeholderKey)"
            rows="5"
          />
        </label>

        <button class="analyze-button" type="submit" :disabled="isAnalyzing">
          {{ isAnalyzing ? t("pages.talentProfile.actions.analyzing") : t("pages.talentProfile.actions.analyze") }}
        </button>

        <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
      </form>

      <section
        v-if="analysis"
        class="report-panel"
        :aria-label="t('pages.talentProfile.report.ariaLabel')"
      >
        <article class="identity-card">
          <span class="card-label">{{ t("pages.talentProfile.report.careerIdentity") }}</span>
          <p>{{ analysis.career_identity }}</p>
        </article>

        <div class="report-grid">
          <article
            v-for="card in reportCards"
            :key="card.title"
            class="report-card"
          >
            <span class="card-label">{{ card.title }}</span>
            <ul>
              <li v-for="item in card.items" :key="item">{{ item }}</li>
            </ul>
          </article>
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
import { computed, reactive, ref } from "vue";
import { useI18n } from "vue-i18n";

import { analyzeProfile, type ProfileAnalysisResponse } from "../services/api";

const { t } = useI18n();

type FormKey = "education" | "skills" | "projects" | "target_roles";

const fields: Array<{
  key: FormKey;
  labelKey: string;
  placeholderKey: string;
}> = [
  {
    key: "education",
    labelKey: "pages.talentProfile.fields.education.label",
    placeholderKey: "pages.talentProfile.fields.education.placeholder"
  },
  {
    key: "skills",
    labelKey: "pages.talentProfile.fields.skills.label",
    placeholderKey: "pages.talentProfile.fields.skills.placeholder"
  },
  {
    key: "projects",
    labelKey: "pages.talentProfile.fields.projects.label",
    placeholderKey: "pages.talentProfile.fields.projects.placeholder"
  },
  {
    key: "target_roles",
    labelKey: "pages.talentProfile.fields.targetRoles.label",
    placeholderKey: "pages.talentProfile.fields.targetRoles.placeholder"
  }
];

const form = reactive<Record<FormKey, string>>({
  education: "",
  skills: "",
  projects: "",
  target_roles: ""
});

const analysis = ref<ProfileAnalysisResponse | null>(null);
const isAnalyzing = ref(false);
const errorMessage = ref("");

const toLines = (value: string): string[] => {
  return value
    .split("\n")
    .map((line) => line.trim())
    .filter(Boolean);
};

const reportCards = computed(() => {
  if (!analysis.value) {
    return [];
  }

  return [
    { title: t("pages.talentProfile.report.capabilities"), items: analysis.value.capabilities },
    { title: t("pages.talentProfile.report.evidence"), items: analysis.value.evidence },
    { title: t("pages.talentProfile.report.strengths"), items: analysis.value.strengths },
    { title: t("pages.talentProfile.report.gaps"), items: analysis.value.gaps },
    { title: t("pages.talentProfile.report.recommendedRoles"), items: analysis.value.recommended_roles }
  ];
});

const handleAnalyze = async () => {
  isAnalyzing.value = true;
  errorMessage.value = "";

  try {
    analysis.value = await analyzeProfile({
      education: toLines(form.education),
      skills: toLines(form.skills),
      projects: toLines(form.projects),
      target_roles: toLines(form.target_roles)
    });
  } catch {
    errorMessage.value = t("pages.talentProfile.errors.analysisFailed");
  } finally {
    isAnalyzing.value = false;
  }
};
</script>

<style scoped>
.talent-profile {
  max-width: 1180px;
}

.profile-header {
  margin-bottom: 28px;
}

.profile-workspace {
  display: grid;
  grid-template-columns: minmax(300px, 420px) 1fr;
  gap: 24px;
  align-items: start;
}

.profile-form,
.empty-report,
.identity-card,
.report-card {
  border: 1px solid #dedbd2;
  border-radius: 8px;
  background: #fff;
  box-shadow: 0 1px 2px rgb(17 24 39 / 5%);
}

.profile-form {
  display: grid;
  gap: 18px;
  padding: 20px;
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
  cursor: progress;
  opacity: 0.72;
}

.error-message {
  margin: 0;
  color: #b91c1c;
  font-size: 14px;
  line-height: 1.5;
}

.report-panel {
  display: grid;
  gap: 18px;
}

.identity-card,
.report-card,
.empty-report {
  padding: 20px;
}

.identity-card p,
.empty-report p {
  margin: 10px 0 0;
  color: #374151;
  font-size: 16px;
  line-height: 1.65;
}

.card-label {
  color: #6b7280;
  font-size: 12px;
  font-weight: 750;
  letter-spacing: 0;
  text-transform: uppercase;
}

.report-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 18px;
}

.report-card ul {
  display: grid;
  gap: 10px;
  margin: 12px 0 0;
  padding-left: 18px;
  color: #374151;
  line-height: 1.5;
}

.empty-report {
  min-height: 280px;
}

@media (max-width: 980px) {
  .profile-workspace,
  .report-grid {
    grid-template-columns: 1fr;
  }
}
</style>

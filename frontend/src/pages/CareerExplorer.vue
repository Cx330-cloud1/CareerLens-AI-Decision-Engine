<template>
  <section class="page-section explorer-page">
    <header class="page-header explorer-header">
      <div class="page-header__meta">
        <span class="status-token">Career Explorer</span>
        <span class="status-token status-token--neutral">{{ templates.length }} role templates</span>
      </div>
      <h1>Explore career paths through reusable role knowledge</h1>
      <p class="lede">
        Browse structured role templates before running Role Intelligence and downstream alignment.
      </p>
    </header>

    <div class="explorer-layout">
      <WorkspacePanel class="explorer-controls">
        <label class="field-group">
          <span>Search roles</span>
          <input v-model="searchQuery" placeholder="Product analyst, backend, data, operations" />
        </label>

        <div class="category-list" aria-label="Career categories">
          <button
            type="button"
            :class="{ active: selectedCategoryId === '' }"
            @click="selectedCategoryId = ''"
          >
            <strong>All roles</strong>
            <span>{{ allTemplateCount }}</span>
          </button>
          <button
            v-for="category in categories"
            :key="category.category_id"
            type="button"
            :class="{ active: selectedCategoryId === category.category_id }"
            @click="selectedCategoryId = category.category_id"
          >
            <strong>{{ category.name }}</strong>
            <span>{{ category.role_count }}</span>
          </button>
        </div>

        <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
      </WorkspacePanel>

      <section class="template-list" aria-label="Role templates">
        <article
          v-for="template in filteredTemplates"
          :key="template.template_id"
          :class="['template-card', { active: selectedTemplateId === template.template_id }]"
          @click="selectedTemplateId = template.template_id"
        >
          <div class="card-topline">
            <strong>{{ template.title }}</strong>
            <span>{{ template.seniority }}</span>
          </div>
          <p>{{ template.summary }}</p>
          <div class="tag-row">
            <span>{{ template.role_family }}</span>
            <span>{{ categoryName(template.category_id) }}</span>
            <span>{{ template.capability_mappings.length }} capabilities</span>
          </div>
        </article>

        <EmptyState
          v-if="!isLoading && filteredTemplates.length === 0"
          eyebrow="No matching template"
          title="Adjust search or category"
          description="CareerLens currently ships with a focused seed library. More roles can be added through the role knowledge service."
        />
      </section>

      <WorkspacePanel v-if="selectedTemplate" class="template-detail">
        <div class="section-heading">
          <span class="section-kicker">Role template</span>
          <RouterLink
            class="secondary-button"
            :to="{ path: '/role-intelligence', query: { template_id: selectedTemplate.template_id } }"
          >
            Use in Role Intelligence
          </RouterLink>
        </div>

        <div class="detail-heading">
          <h2>{{ selectedTemplate.title }}</h2>
          <p>{{ selectedTemplate.business_context }}</p>
        </div>

        <div class="metric-grid">
          <MetricBlock
            label="Responsibilities"
            :value="selectedTemplate.responsibilities.length"
            detail="Template scope"
          />
          <MetricBlock
            label="Capabilities"
            :value="selectedTemplate.capability_mappings.length"
            detail="Mapped requirements"
          />
          <MetricBlock
            label="Common gaps"
            :value="selectedTemplate.common_gaps.length"
            detail="Alignment risks"
            variant="accent"
          />
        </div>

        <section class="detail-section">
          <div class="section-heading">
            <span class="section-kicker">Capability map</span>
            <strong>{{ selectedTemplate.capability_mappings.length }}</strong>
          </div>
          <article
            v-for="mapping in selectedTemplate.capability_mappings"
            :key="mapping.mapping_id"
            class="mapping-row"
          >
            <div class="card-topline">
              <strong>{{ mapping.capability.name }}</strong>
              <span>{{ mapping.importance }}</span>
            </div>
            <p>{{ mapping.capability.description }}</p>
            <div class="evidence-grid">
              <div>
                <span>Evidence examples</span>
                <ul>
                  <li v-for="item in mapping.evidence_examples" :key="item">{{ item }}</li>
                </ul>
              </div>
              <div>
                <span>Development actions</span>
                <ul>
                  <li v-for="item in mapping.development_actions" :key="item">{{ item }}</li>
                </ul>
              </div>
            </div>
          </article>
        </section>
      </WorkspacePanel>

      <WorkspacePanel v-else class="template-detail loading-detail">
        <span class="section-kicker">Role template</span>
        <p>{{ isLoading ? "Loading role knowledge..." : "Select a role template to inspect details." }}</p>
      </WorkspacePanel>
    </div>
  </section>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from "vue";

import EmptyState from "../components/EmptyState.vue";
import MetricBlock from "../components/MetricBlock.vue";
import WorkspacePanel from "../components/WorkspacePanel.vue";
import { getRoleTemplates, type CareerCategory, type RoleTemplate } from "../services/api";

const categories = ref<CareerCategory[]>([]);
const templates = ref<RoleTemplate[]>([]);
const selectedCategoryId = ref("");
const selectedTemplateId = ref("");
const searchQuery = ref("");
const isLoading = ref(true);
const errorMessage = ref("");

const allTemplateCount = computed(() => templates.value.length);
const filteredTemplates = computed(() => {
  const query = searchQuery.value.trim().toLowerCase();
  return templates.value.filter((template) => {
    const matchesCategory =
      !selectedCategoryId.value || template.category_id === selectedCategoryId.value;
    const matchesSearch =
      !query ||
      template.title.toLowerCase().includes(query) ||
      template.summary.toLowerCase().includes(query) ||
      template.role_family.toLowerCase().includes(query);
    return matchesCategory && matchesSearch;
  });
});
const selectedTemplate = computed(
  () => templates.value.find((template) => template.template_id === selectedTemplateId.value) ?? null
);

function categoryName(categoryId: string): string {
  return categories.value.find((category) => category.category_id === categoryId)?.name ?? categoryId;
}

onMounted(async () => {
  try {
    const response = await getRoleTemplates();
    categories.value = response.categories;
    templates.value = response.templates;
    selectedTemplateId.value = response.templates[0]?.template_id ?? "";
  } catch {
    errorMessage.value = "Career Explorer failed to load role templates.";
  } finally {
    isLoading.value = false;
  }
});
</script>

<style scoped>
.explorer-page,
.explorer-header {
  max-width: 1320px;
}

.explorer-layout {
  display: grid;
  grid-template-columns: 260px minmax(260px, 0.78fr) minmax(420px, 1.22fr);
  gap: 18px;
  align-items: start;
}

.explorer-controls,
.template-detail {
  position: sticky;
  top: 24px;
}

.explorer-controls,
.template-detail,
.detail-section,
.mapping-row,
.detail-heading {
  display: grid;
  gap: 16px;
}

.explorer-controls,
.template-detail {
  padding: 20px;
}

.category-list,
.template-list {
  display: grid;
  gap: 10px;
}

.category-list button {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 10px;
  align-items: center;
  min-height: 42px;
  border: 1px solid var(--border);
  border-radius: 8px;
  background: var(--surface);
  color: var(--text-muted);
  cursor: pointer;
  padding: 10px 12px;
  text-align: left;
}

.category-list button.active {
  border-color: #202321;
  background: #202321;
  color: #fffefa;
}

.category-list strong,
.category-list span {
  font-size: 13px;
  font-weight: 760;
}

.template-card,
.mapping-row {
  display: grid;
  gap: 12px;
  border: 1px solid var(--border);
  border-radius: 8px;
  background: var(--surface);
  padding: 16px;
}

.template-card {
  cursor: pointer;
}

.template-card:hover,
.template-card.active {
  border-color: var(--border-strong);
  background: var(--surface-subtle);
}

.template-card.active {
  box-shadow: inset 3px 0 0 var(--accent);
}

.template-card p,
.detail-heading p,
.mapping-row p,
.loading-detail p,
.evidence-grid li {
  margin: 0;
  color: var(--text-muted);
  font-size: 14px;
  line-height: 1.55;
}

.detail-heading p {
  max-width: 74ch;
}

.evidence-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 12px;
}

.evidence-grid div {
  display: grid;
  gap: 8px;
  border: 1px solid var(--border);
  border-radius: 8px;
  background: var(--surface-subtle);
  padding: 12px;
}

.evidence-grid span {
  color: var(--text-soft);
  font-size: 11px;
  font-weight: 760;
  text-transform: uppercase;
}

.evidence-grid ul {
  display: grid;
  gap: 8px;
  margin: 0;
  padding-left: 18px;
}

@media (max-width: 1180px) {
  .explorer-layout {
    grid-template-columns: 1fr;
  }

  .explorer-controls,
  .template-detail {
    position: static;
  }
}

@media (max-width: 680px) {
  .evidence-grid {
    grid-template-columns: 1fr;
  }
}
</style>

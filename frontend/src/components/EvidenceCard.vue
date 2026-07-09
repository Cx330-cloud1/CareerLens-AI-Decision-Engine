<template>
  <WorkspacePanel class="evidence-card">
    <div class="evidence-card__header">
      <span class="section-kicker">{{ source }}</span>
      <strong>{{ strength }}</strong>
    </div>
    <p>{{ excerpt }}</p>
    <div v-if="capability || relevance" class="evidence-card__context">
      <div v-if="capability">
        <span>Capability demonstrated</span>
        <strong>{{ capability }}</strong>
      </div>
      <div v-if="relevance">
        <span>Role relevance</span>
        <strong>{{ relevance }}</strong>
      </div>
    </div>
    <ConfidenceMeter :value="confidence" label="Evidence confidence" />
  </WorkspacePanel>
</template>

<script setup lang="ts">
import ConfidenceMeter from "./ConfidenceMeter.vue";
import WorkspacePanel from "./WorkspacePanel.vue";

defineProps<{
  source: string;
  strength: string;
  excerpt: string;
  confidence: number;
  capability?: string;
  relevance?: string;
}>();
</script>

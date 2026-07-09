<template>
  <WorkspacePanel class="metric-block" :variant="variant">
    <span class="metric-block__label">{{ label }}</span>
    <strong class="metric-block__value">{{ value }}</strong>
    <span v-if="detail" class="metric-block__detail">{{ detail }}</span>
  </WorkspacePanel>
</template>

<script setup lang="ts">
import WorkspacePanel from "./WorkspacePanel.vue";

defineProps<{
  label: string;
  value: string | number;
  detail?: string;
  variant?: "muted" | "accent" | "danger";
}>();
</script>

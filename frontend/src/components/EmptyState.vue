<template>
  <WorkspacePanel class="empty-state" variant="muted">
    <span class="section-kicker">{{ eyebrow }}</span>
    <h2>{{ title }}</h2>
    <p>{{ description }}</p>
    <slot />
  </WorkspacePanel>
</template>

<script setup lang="ts">
import WorkspacePanel from "./WorkspacePanel.vue";

defineProps<{
  eyebrow: string;
  title: string;
  description: string;
}>();
</script>

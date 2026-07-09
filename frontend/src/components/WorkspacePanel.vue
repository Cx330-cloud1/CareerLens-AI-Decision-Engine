<template>
  <article :class="['workspace-panel', variant ? `workspace-panel--${variant}` : '']">
    <slot />
  </article>
</template>

<script setup lang="ts">
defineProps<{
  variant?: "muted" | "accent" | "danger";
}>();
</script>

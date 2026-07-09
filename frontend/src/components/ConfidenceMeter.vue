<template>
  <div class="confidence-meter" :aria-label="`${label}: ${percent}%`">
    <div class="confidence-meter__topline">
      <span>{{ label }}</span>
      <strong>{{ percent }}%</strong>
    </div>
    <div class="confidence-meter__track">
      <span :style="{ width: `${percent}%` }" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from "vue";

const props = withDefaults(
  defineProps<{
    value: number;
    label?: string;
  }>(),
  {
    label: "Confidence"
  }
);

const percent = computed(() => {
  const normalized = props.value <= 1 ? props.value * 100 : props.value;
  return Math.min(100, Math.max(0, Math.round(normalized)));
});
</script>

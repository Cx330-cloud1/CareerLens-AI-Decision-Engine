<template>
  <section class="page-section">
    <p class="eyebrow">{{ t("pages.careerPlan.eyebrow") }}</p>
    <h1>{{ t("pages.careerPlan.title") }}</h1>
    <p class="lede">{{ t("pages.careerPlan.lede") }}</p>
  </section>
</template>

<script setup lang="ts">
import { useI18n } from "vue-i18n";

const { t } = useI18n();
</script>

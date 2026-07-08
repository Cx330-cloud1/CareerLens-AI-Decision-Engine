<template>
  <section class="page-section">
    <p class="eyebrow">{{ t("pages.matchReport.eyebrow") }}</p>
    <h1>{{ t("pages.matchReport.title") }}</h1>
    <p class="lede">{{ t("pages.matchReport.lede") }}</p>
  </section>
</template>

<script setup lang="ts">
import { useI18n } from "vue-i18n";

const { t } = useI18n();
</script>

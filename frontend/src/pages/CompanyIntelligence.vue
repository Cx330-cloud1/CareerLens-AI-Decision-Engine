<template>
  <section class="page-section">
    <p class="eyebrow">{{ t("pages.companyIntelligence.eyebrow") }}</p>
    <h1>{{ t("pages.companyIntelligence.title") }}</h1>
    <p class="lede">{{ t("pages.companyIntelligence.lede") }}</p>
  </section>
</template>

<script setup lang="ts">
import { useI18n } from "vue-i18n";

const { t } = useI18n();
</script>

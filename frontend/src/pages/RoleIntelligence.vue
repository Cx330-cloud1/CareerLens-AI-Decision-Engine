<template>
  <section class="page-section">
    <p class="eyebrow">{{ t("pages.roleIntelligence.eyebrow") }}</p>
    <h1>{{ t("pages.roleIntelligence.title") }}</h1>
    <p class="lede">{{ t("pages.roleIntelligence.lede") }}</p>
  </section>
</template>

<script setup lang="ts">
import { useI18n } from "vue-i18n";

const { t } = useI18n();
</script>

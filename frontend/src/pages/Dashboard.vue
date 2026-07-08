<template>
  <section class="page-section">
    <p class="eyebrow">{{ t("pages.dashboard.eyebrow") }}</p>
    <h1>{{ t("pages.dashboard.title") }}</h1>
    <dl class="status-list">
      <div class="status-row">
        <dt>{{ t("pages.dashboard.backend") }}</dt>
        <dd :class="backendConnected ? 'connected' : 'disconnected'">
          {{ backendConnected ? t("pages.dashboard.connected") : t("pages.dashboard.disconnected") }}
        </dd>
      </div>
    </dl>
  </section>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";
import { useI18n } from "vue-i18n";

import { getBackendHealth } from "../services/api";

const { t } = useI18n();
const backendConnected = ref(false);

onMounted(async () => {
  try {
    await getBackendHealth();
    backendConnected.value = true;
  } catch {
    backendConnected.value = false;
  }
});
</script>

<style scoped>
.status-list {
  display: grid;
  gap: 12px;
  margin: 28px 0 0;
}

.status-row {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 18px;
}

.status-row dt {
  color: #374151;
  font-weight: 650;
}

.status-row dd {
  margin: 0;
  font-weight: 650;
}

.connected {
  color: #047857;
}

.disconnected {
  color: #b91c1c;
}
</style>

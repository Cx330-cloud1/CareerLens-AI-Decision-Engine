<script setup lang="ts">
import { computed } from "vue";
import { useI18n } from "vue-i18n";

import { setLocale, supportedLocales, type SupportedLocale } from "./i18n";

const navigation = [
  { key: "navigation.dashboard", path: "/" },
  { key: "navigation.talentProfile", path: "/talent-profile" },
  { key: "navigation.companyIntelligence", path: "/company-intelligence" },
  { key: "navigation.roleIntelligence", path: "/role-intelligence" },
  { key: "navigation.matchReport", path: "/match-report" },
  { key: "navigation.careerPlan", path: "/career-plan" }
];

const { locale, t } = useI18n({ useScope: "global" });

const currentLocale = computed({
  get: () => locale.value as SupportedLocale,
  set: (value: SupportedLocale) => setLocale(value)
});
</script>

<template>
  <div class="app-shell">
    <aside class="sidebar">
      <div class="brand">
        CareerLens
      </div>

      <nav class="nav-list">
        <RouterLink
          v-for="item in navigation"
          :key="item.path"
          :to="item.path"
        >
          {{ t(item.key) }}
        </RouterLink>
      </nav>

      <label class="language-switcher">
        <span>{{ t("language.label") }}</span>
        <select v-model="currentLocale">
          <option
            v-for="localeOption in supportedLocales"
            :key="localeOption"
            :value="localeOption"
          >
            {{ t(localeOption === "zh-CN" ? "language.zhCN" : "language.enUS") }}
          </option>
        </select>
      </label>
    </aside>

    <main class="main-panel">
      <RouterView />
    </main>
  </div>
</template>

<style scoped>
.app-shell {
  display: flex;
  min-height: 100vh;
}

.sidebar {
  width: 240px;
  padding: 24px;
  border-right: 1px solid #eee;
}

.nav-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.language-switcher {
  display: grid;
  gap: 8px;
  margin-top: 28px;
  color: #4b5563;
  font-size: 13px;
  font-weight: 650;
}

.language-switcher select {
  width: 100%;
  border: 1px solid #d1d5db;
  border-radius: 8px;
  background: #fff;
  color: #111827;
  font: inherit;
  font-weight: 500;
  padding: 8px 10px;
}

.main-panel {
  flex: 1;
  padding: 32px;
}
</style>

<script setup lang="ts">
import { computed } from "vue";
import { useI18n } from "vue-i18n";

import { setLocale, supportedLocales, type SupportedLocale } from "./i18n";

const navigation = [
  {
    key: "navigation.dashboard",
    descriptionKey: "navigationDescriptions.dashboard",
    path: "/",
    marker: "01"
  },
  {
    key: "navigation.talentProfile",
    descriptionKey: "navigationDescriptions.talentProfile",
    path: "/talent-profile",
    marker: "02"
  },
  {
    key: "navigation.careerExplorer",
    descriptionKey: "navigationDescriptions.careerExplorer",
    path: "/career-explorer",
    marker: "03"
  },
  {
    key: "navigation.roleIntelligence",
    descriptionKey: "navigationDescriptions.roleIntelligence",
    path: "/role-intelligence",
    marker: "04"
  },
  {
    key: "navigation.matchReport",
    descriptionKey: "navigationDescriptions.matchReport",
    path: "/match-report",
    marker: "05"
  },
  {
    key: "navigation.resumeOptimization",
    descriptionKey: "navigationDescriptions.resumeOptimization",
    path: "/resume-optimization",
    marker: "06"
  },
  {
    key: "navigation.careerPlan",
    descriptionKey: "navigationDescriptions.careerPlan",
    path: "/career-plan",
    marker: "07"
  }
];

const { locale, t } = useI18n({ useScope: "global" });

const currentLocale = computed({
  get: () => locale.value as SupportedLocale,
  set: (value: SupportedLocale) => setLocale(value)
});
</script>

<template>
  <div class="app-shell">
    <a class="skip-link" href="#workspace-content">Skip to workspace</a>

    <aside class="sidebar" aria-label="CareerLens workspace navigation">
      <div class="brand-lockup">
        <div class="brand-mark" aria-hidden="true">CL</div>
        <div>
          <div class="brand">CareerLens</div>
          <p>Career intelligence workspace</p>
        </div>
      </div>

      <div class="workspace-status">
        <span class="section-kicker">Active workflow</span>
        <strong>Resume to role fit</strong>
        <p>Structured inputs, evidence-backed analysis, and explainable recommendations.</p>
      </div>

      <nav class="nav-list">
        <RouterLink
          v-for="item in navigation"
          :key="item.path"
          :to="item.path"
        >
          <span class="nav-marker">{{ item.marker }}</span>
          <span>
            <strong>{{ t(item.key) }}</strong>
            <small>{{ t(item.descriptionKey) }}</small>
          </span>
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

    <main id="workspace-content" class="main-panel">
      <RouterView />
    </main>
  </div>
</template>

<style scoped>
.app-shell {
  display: grid;
  grid-template-columns: 286px minmax(0, 1fr);
}

.skip-link {
  position: fixed;
  left: 16px;
  top: 12px;
  z-index: 10;
  border-radius: 8px;
  background: #202321;
  color: #fffefa;
  font-size: 13px;
  font-weight: 750;
  padding: 9px 12px;
  transform: translateY(-160%);
}

.skip-link:focus {
  transform: translateY(0);
}

.sidebar {
  position: sticky;
  top: 0;
  display: grid;
  align-content: start;
  gap: 22px;
  min-height: 100dvh;
  border-right: 1px solid var(--border);
  background: rgb(251 250 247 / 90%);
  backdrop-filter: blur(18px);
  padding: 20px;
}

.brand-lockup {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 12px;
  align-items: center;
}

.brand-mark {
  display: grid;
  width: 42px;
  height: 42px;
  place-items: center;
  border: 1px solid #202321;
  border-radius: 10px;
  background: #202321;
  color: #fffefa;
  font-size: 13px;
  font-weight: 800;
  letter-spacing: -0.03em;
}

.brand {
  color: var(--text);
  font-size: 18px;
  font-weight: 780;
  letter-spacing: -0.02em;
}

.brand-lockup p,
.workspace-status p,
.nav-list small {
  margin: 0;
  color: var(--text-muted);
  font-size: 12px;
  line-height: 1.45;
}

.workspace-status {
  display: grid;
  gap: 7px;
  border: 1px solid var(--border);
  border-radius: 10px;
  background: var(--surface);
  padding: 14px;
}

.workspace-status strong {
  color: var(--text);
  font-size: 15px;
  letter-spacing: -0.01em;
}

.nav-list {
  display: grid;
  gap: 4px;
}

.nav-list a {
  display: grid;
  grid-template-columns: 30px 1fr;
  gap: 10px;
  align-items: start;
  border-radius: 8px;
  color: #555852;
  padding: 9px 10px;
}

.nav-list a:hover {
  background: #f0eee8;
}

.nav-list a.router-link-active {
  background: #202321;
  color: #fffefa;
}

.nav-list a.router-link-active small,
.nav-list a.router-link-active .nav-marker {
  color: rgb(255 254 250 / 72%);
}

.nav-list strong {
  display: block;
  margin-bottom: 2px;
  font-size: 14px;
  line-height: 1.2;
}

.nav-marker {
  color: var(--text-soft);
  font-size: 11px;
  font-weight: 800;
  font-variant-numeric: tabular-nums;
  line-height: 1.4;
}

.language-switcher {
  display: grid;
  gap: 8px;
  margin-top: 8px;
  color: var(--text-muted);
  font-size: 12px;
  font-weight: 750;
}

.language-switcher select {
  width: 100%;
  border: 1px solid var(--border-strong);
  border-radius: 8px;
  background: var(--surface);
  color: var(--text);
  font-weight: 650;
  padding: 9px 10px;
}

.main-panel {
  padding: 30px clamp(22px, 3vw, 42px) 48px;
}

@media (max-width: 920px) {
  .app-shell {
    grid-template-columns: 1fr;
  }

  .sidebar {
    position: static;
    min-height: auto;
    border-right: 0;
    border-bottom: 1px solid var(--border);
  }

  .workspace-status {
    display: none;
  }

  .nav-list {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 560px) {
  .sidebar {
    padding: 18px;
  }

  .nav-list {
    grid-template-columns: 1fr;
  }

  .main-panel {
    padding: 26px 16px 42px;
  }
}
</style>

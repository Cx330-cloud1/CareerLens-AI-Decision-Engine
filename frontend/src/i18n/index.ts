import { createI18n } from "vue-i18n";

import enUS from "../locales/en-US";
import zhCN from "../locales/zh-CN";

export const supportedLocales = ["zh-CN", "en-US"] as const;

export type SupportedLocale = (typeof supportedLocales)[number];

const localeStorageKey = "careerlens.locale";

const isSupportedLocale = (locale: string | null): locale is SupportedLocale => {
  return supportedLocales.includes(locale as SupportedLocale);
};

const getDefaultLocale = (): SupportedLocale => {
  const savedLocale = window.localStorage.getItem(localeStorageKey);

  if (isSupportedLocale(savedLocale)) {
    return savedLocale;
  }

  const browserLocales = [navigator.language, ...navigator.languages];
  return browserLocales.some((locale) => locale.toLowerCase().startsWith("zh"))
    ? "zh-CN"
    : "en-US";
};

const i18n = createI18n({
  legacy: false,
  locale: getDefaultLocale(),
  fallbackLocale: "en-US",
  messages: {
    "zh-CN": zhCN,
    "en-US": enUS
  }
});

export const setLocale = (locale: SupportedLocale) => {
  i18n.global.locale.value = locale;
  window.localStorage.setItem(localeStorageKey, locale);
};

export default i18n;

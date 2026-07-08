// if the plugin was ESM compatible, we could use await import('@shopify/prettier-plugin-liquid') instead of shimming in require
// https://stackoverflow.com/questions/69099763/referenceerror-require-is-not-defined-in-es-module-scope-you-can-use-import-in
import { createRequire } from "module";
const require = createRequire(import.meta.url);

// Allow Prettier in .pre-commit-config.yaml to find plugins.
// https://stackoverflow.com/questions/78708497/prettier-plugins-not-found-with-pre-commit
// https://github.com/prettier/prettier/issues/15085
const config = {
  plugins: [require.resolve("@shopify/prettier-plugin-liquid")],
  printWidth: 120,
  tabWidth: 2,
  useTabs: false,
};

export default config;

/**
 * Run `build` or `dev` with `SKIP_ENV_VALIDATION` to skip env validation. This is especially useful
 * for Docker builds.
 */
// Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
// SPDX-License-Identifier: MIT

import "./src/env.js";

/** @type {import("next").NextConfig} */

// DeerFlow leverages **Turbopack** during development for faster builds and a smoother developer experience.
// However, in production, **Webpack** is used instead.
//
// This decision is based on the current recommendation to avoid using Turbopack for critical projects, as it
// is still evolving and may not yet be fully stable for production environments.

const config = {
  // For development mode
  turbopack: {
    rules: {
      "*.md": {
        loaders: ["raw-loader"],
        as: "*.js",
      },
    },
  },

  // For production mode
  webpack: (config) => {
    config.module.rules.push({
      test: /\.md$/,
      use: "raw-loader",
    });
    return config;
  },

  // ... rest of the configuration.
  output: process.env.TAURI_BUILD ? "export" : "standalone",
  trailingSlash: process.env.TAURI_BUILD ? true : false,
  distDir: process.env.TAURI_BUILD ? "out" : ".next",
  assetPrefix: process.env.TAURI_BUILD ? "" : undefined,
  images: {
    unoptimized: process.env.TAURI_BUILD ? true : false,
  },
  typescript: {
    // Skip TypeScript checking during Tauri build to avoid webpack chunk issues
    ignoreBuildErrors: process.env.TAURI_BUILD ? true : false,
  },
  eslint: {
    // Skip ESLint during Tauri build to speed up the process
    ignoreDuringBuilds: process.env.TAURI_BUILD ? true : false,
  },
};

export default config;

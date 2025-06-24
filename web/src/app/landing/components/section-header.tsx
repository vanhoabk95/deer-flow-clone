// Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
// SPDX-License-Identifier: MIT

export function SectionHeader({
  anchor,
  title,
  description,
}: {
  anchor?: string;
  title: React.ReactNode;
  description: React.ReactNode;
}) {
  return (
    <>
      {anchor && <a id={anchor} className="absolute -top-20" />}
      <div className="mb-12 flex flex-col items-center justify-center gap-2">
        <h2 className="mb-4 bg-gradient-to-r from-gray-900 via-gray-700 to-gray-500 dark:from-white dark:via-gray-200 dark:to-gray-400 bg-clip-text text-center text-5xl font-bold text-transparent">
          {title}
        </h2>
        <p className="text-muted-foreground text-center text-xl">
          {description}
        </p>
      </div>
    </>
  );
}

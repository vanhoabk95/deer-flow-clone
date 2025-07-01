// Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
// SPDX-License-Identifier: MIT

import { Bird, Microscope, User } from "lucide-react";
// import { Podcast } from "lucide-react";  // Podcast removed

import { BentoCard, BentoGrid } from "~/components/magicui/bento-grid";

import { SectionHeader } from "../components/section-header";

const features = [
  {
    Icon: Microscope,
    name: "Dive Deeper and Reach Wider",
    description:
      "Unlock deeper insights with advanced tools. Our powerful search + crawling and Python tools gathers comprehensive data, delivering in-depth reports to enhance your study.",
    href: "#",
    cta: "Learn more",
    background: (
      <img alt="background" className="absolute -top-20 -right-20 opacity-60" />
    ),
    className: "lg:col-start-1 lg:col-end-2 lg:row-start-1 lg:row-end-3",
  },
  {
    Icon: User,
    name: "Human-in-the-loop",
    description:
      "Refine your research plan, or adjust focus areas all through simple natural language.",
    href: "#",
    cta: "Learn more",
    background: (
      <img alt="background" className="absolute -top-20 -right-20 opacity-60" />
    ),
    className: "lg:col-start-1 lg:col-end-2 lg:row-start-3 lg:row-end-4",
  },
  {
    Icon: Bird,
    name: "Lang Stack",
    description:
      "Build with confidence using the LangChain and LangGraph frameworks.",
    href: "https://www.langchain.com/",
    cta: "Learn more",
    background: (
      <img alt="background" className="absolute -top-20 -right-20 opacity-60" />
    ),
    className: "lg:col-start-2 lg:col-end-3 lg:row-start-1 lg:row-end-2",
  },
];

export function CoreFeatureSection() {
  return (
    <section className="relative flex w-full flex-col content-around items-center justify-center">
      <SectionHeader
        anchor="core-features"
        title="Core Features"
        description="Find out what makes Development Agent effective."
      />
      <BentoGrid className="w-3/4 lg:grid-cols-2 lg:grid-rows-3">
        {features.map((feature) => (
          <BentoCard key={feature.name} {...feature} />
        ))}
      </BentoGrid>
    </section>
  );
}

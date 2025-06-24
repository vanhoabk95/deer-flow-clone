// Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
// SPDX-License-Identifier: MIT

import { FileSearch, ClipboardPenLine, FlaskConical, ContactRound} from "lucide-react";

import { BentoCard } from "~/components/magicui/bento-grid";

import { SectionHeader } from "../components/section-header";

const caseStudies = [
  {
    title: "1. Issue History Q&A and Root Cause Analysis",
    icon: FileSearch,
    description:
      "Empower your team to quickly investigate past issues by asking natural language questions. The AI agent searches historical records, identifies relevant incidents, and suggests potential root causes based on similar phenomena, accelerating troubleshooting and knowledge transfer.",
  },
  {
    title: "2. Risk Assessment and Change Impact Checklist",
    icon: FlaskConical,
    description:
      "Enhance decision-making when implementing changes. The AI agent analyzes proposed modifications, highlights potential risks, and generates a tailored checklist of items to review—ensuring thorough risk assessment and safer design or process updates."
  },
  {
    title: "3. Interactive Working Guide",
    icon: ClipboardPenLine,
    description:
      "Provide step-by-step guidance for any work task. Users simply ask how to perform specific actions, and the AI agent delivers clear, actionable instructions—reducing onboarding time, supporting continuous learning, and improving workflow efficiency.",
  },
  {
    title: "4. Common Knowledge Q&A: Policies, Training",
    icon: ContactRound,
    description:
      "Centralize answers to everyday organizational questions. The AI agent responds instantly to queries about HR policies, required training, security regulations, and more—helping everyone stay informed and compliant without searching through multiple documents.",
  },
];

export function CaseStudySection() {
  return (
    <section className="relative container hidden flex-col items-center justify-center md:flex">
      <SectionHeader
        anchor="case-studies"
        title="Use Cases"
        description="See examples of what Development Agent can research for you."
      />
      <div className="grid w-3/4 grid-cols-1 gap-2 sm:w-full sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
        {caseStudies.map((caseStudy) => (
          <div key={caseStudy.title} className="w-full p-2">
            <BentoCard
              {...{
                Icon: caseStudy.icon,
                name: caseStudy.title,
                description: caseStudy.description,
                className: "w-full h-full",
              }}
            />
          </div>
        ))}
      </div>
    </section>
  );
}

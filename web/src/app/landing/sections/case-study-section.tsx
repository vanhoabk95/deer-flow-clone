// Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
// SPDX-License-Identifier: MIT

import { Bike, Building, Film, Github, Ham, Home, Pizza } from "lucide-react";
import { Bot } from "lucide-react";

import { BentoCard } from "~/components/magicui/bento-grid";

import { SectionHeader } from "../components/section-header";

const caseStudies = [
  {
    title: "How tall is Eiffel Tower compared to tallest building?",
    icon: Building,
    description:
      "Research compares the heights and global significance of the Eiffel Tower and Burj Khalifa, and uses Python code to calculate the multiples.",
  },
  {
    title: "What are the top trending repositories on GitHub?",
    icon: Github,
    description:
      "Research utilizes tools to identify the most popular GitHub repositories and documents them in detail using search engines.",
  },
  {
    title: "Write an article about Nanjing's traditional dishes",
    icon: Ham,
    description:
      "Study vividly showcases Nanjing's famous dishes through rich content and imagery, uncovering their hidden histories and cultural significance.",
  },
  {
    title: "How to decorate a small rental apartment?",
    icon: Home,
    description:
      "Study provides readers with practical and straightforward methods for decorating apartments, accompanied by inspiring images.",
  },
  {
    title: "Introduce the movie 'Léon: The Professional'",
    icon: Film,
    description:
      "Research provides a comprehensive introduction to the movie 'Léon: The Professional', including its plot, characters, and themes.",
  },
  {
    title: "How do you view the takeaway war in China?",
    icon: Bike,
    description:
      "Research analyzes the intensifying competition between JD and Meituan, highlighting their strategies, technological innovations, and challenges.",
  },
  {
    title: "Are ultra-processed foods linked to health?",
    icon: Pizza,
    description:
      "Research examines the health risks of rising ultra-processed food consumption, urging more research on long-term effects and individual differences.",
  },
  {
    title: 'Write an article on "Would you insure your AI twin?"',
    icon: Bot,
    description:
      "Research explores the concept of insuring AI twins, highlighting their benefits, risks, ethical considerations, and the evolving regulatory.",
  },
];

export function CaseStudySection() {
  return (
    <section className="relative container hidden flex-col items-center justify-center md:flex">
      <SectionHeader
        anchor="case-studies"
        title="Research Examples"
        description="See examples of what DeerFlow can research for you."
      />
      <div className="grid w-3/4 grid-cols-1 gap-2 sm:w-full sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
        {caseStudies.map((caseStudy) => (
          <div key={caseStudy.title} className="w-full p-2">
            <BentoCard
              {...{
                Icon: caseStudy.icon,
                name: caseStudy.title,
                description: caseStudy.description,
                href: `/chat`,
                cta: "Try this research",
                className: "w-full h-full",
              }}
            />
          </div>
        ))}
      </div>
    </section>
  );
}

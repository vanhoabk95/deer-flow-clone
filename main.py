# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT

"""
Entry point script for the DeerFlow project.
"""

import argparse
import asyncio

from src.workflow import run_agent_workflow_async


def ask(
    question,
    debug=False,
    max_plan_iterations=1,
    max_step_num=3,
):
    """Run the agent workflow with the given question.

    Args:
        question: The user's query or request
        debug: If True, enables debug level logging
        max_plan_iterations: Maximum number of plan iterations
        max_step_num: Maximum number of steps in a plan
    """
    asyncio.run(
        run_agent_workflow_async(
            user_input=question,
            debug=debug,
            max_plan_iterations=max_plan_iterations,
            max_step_num=max_step_num,
        )
    )


if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Run the Deer")
    parser.add_argument("query", nargs="*", help="The query to process")
    parser.add_argument(
        "--max_plan_iterations",
        type=int,
        default=1,
        help="Maximum number of plan iterations (default: 1)",
    )
    parser.add_argument(
        "--max_step_num",
        type=int,
        default=3,
        help="Maximum number of steps in a plan (default: 3)",
    )
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")


    args = parser.parse_args()

    # Parse user input from command line arguments or user input
    if args.query:
        user_query = " ".join(args.query)
    else:
        user_query = input("Enter your query: ")

    # Run the agent workflow with the provided parameters
    ask(
        question=user_query,
        debug=args.debug,
        max_plan_iterations=args.max_plan_iterations,
        max_step_num=args.max_step_num,
    )

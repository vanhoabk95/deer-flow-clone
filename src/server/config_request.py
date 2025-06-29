# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT

from pydantic import BaseModel, Field


class ConfigResponse(BaseModel):
    """Response model for server config."""

    models: dict[str, list[str]] = Field(..., description="The configured models")

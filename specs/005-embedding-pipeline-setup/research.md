# Research: Embedding Pipeline Setup (Updated)

This document outlines the decisions made to resolve unknowns during the planning phase.

## 1. Target Docusaurus URL

-   **Initial Unknown**: The specific URL of the deployed Docusaurus site to be crawled was not provided in the initial feature specification. The initial decision was to use a configurable placeholder.
-   **Update**: The user has provided the explicit target URL during the planning phase.
-   **Decision**: The pipeline will be implemented to target the following URL: `https://physical-ai-humanoid-robotics-ww8u.vercel.app/`. While it will be coded directly for this target, it should still be stored in a constant or configuration variable for maintainability.
-   **Rationale**: The requirement is now explicit. Using a variable for the URL remains good practice.
-   **Alternatives considered**: None required, as the ambiguity has been resolved.


Run the notebook and complete the following:

  - Task 1: Dependencies and Set-Up
  - Task 2: Setting up Production RAG and LangGraph Agent Integration
  - Task 3: Guardrails Integration for Production Safety

## Guard Rails Set-up

### 1. Install Dependencies

```bash
uv sync
```

### 2. Configure Guardrails API

```bash
uv run guardrails configure
```

Provide your Guardrails AI API key, found [here](https://hub.guardrailsai.com/keys).

### 3. Install Required Guards

```bash
uv run guardrails hub install hub://tryolabs/restricttotopic
uv run guardrails hub install hub://guardrails/detect_jailbreak
uv run guardrails hub install hub://guardrails/competitor_check
uv run guardrails hub install hub://arize-ai/llm_rag_evaluator
uv run guardrails hub install hub://guardrails/profanity_free
uv run guardrails hub install hub://guardrails/guardrails_pii
```

## 🚧 Advanced Build:

<details>
<summary>🚧 Advanced Build 🚧 (OPTIONAL - <i>open this section for the requirements</i>)</summary>

The caching we're using is both: 

1. Ineffecient
2. Exact Match

Please produce a locally running application (through Docker) that integrates a more intelligent caching process.

In simpler terms: 

- Use a database approach (Redis, Vectordatase, SQLite, etc.) instead of plain-memory for caching
- Implement Semantic LLM Caching OR Implement E2E Caching
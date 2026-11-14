# STEM Link RAG

A hands-on learning project exploring how to build an agricultural assistant for Sri Lankan paddy farmers with Python, LangChain, and OpenAI models. The examples move from basic chat calls to conversation history, model settings, grounding answers in a small reference corpus, and calling a live weather tool.

**Developer:** DKCN Nipuna Gomes

> **Project status:** This repository is currently a collection of tutorial scripts, not a complete retrieval-augmented generation (RAG) application. The corpus in `scripts/corpus.py` is added directly to a prompt in the grounding example; there is not yet a document loader, vector store, or retrieval pipeline.

## What's included

- **OpenAI and LangChain wrappers** - introductory examples for calling a chat model (`scripts/00_providers_wrappers.py`).
- **Chat messages and conversation context** - role-based messages, follow-up questions, and how prior assistant messages affect a response (`scripts/01_chat_and_messages.py`).
- **Temperature and top-p** - examples of model sampling settings (`scripts/02_temparature_and_top_p.py`).
- **Grounding and limitations** - passes a small paddy cultivation corpus into the prompt and asks the model to answer from those passages (`scripts/03_limitations.py`, `scripts/corpus.py`).
- **Tool calling and weather** - lets the model request a 24-hour rainfall forecast for a place using Open-Meteo (`scripts/04_tools_and_toolnode.py`, `scripts/weather.py`).

The sample corpus covers topics such as Sri Lankan rice varieties, fertilizer schedules, seed rates, water management, and cultivation seasons. It is an educational sample and should not replace current, locally applicable agricultural guidance.

## Requirements

- Python 3.13 or later
- [uv](https://docs.astral.sh/uv/) for environment and dependency management
- An OpenAI API key for the model examples
- Internet access for OpenAI requests and the Open-Meteo weather example

## Setup

Clone the repository, then from its root directory run:

```powershell
uv sync
```

Create a `.env` file in the repository root and add your OpenAI API key:

```dotenv
OPENAI_API_KEY=your_api_key_here
```

The scripts load this file automatically. Keep the key private; `.env` is excluded from Git.

## Run the examples

Run scripts from the repository root with `uv`:

```powershell
uv run python scripts/00_providers_wrappers.py
uv run python scripts/01_chat_and_messages.py
uv run python scripts/02_temparature_and_top_p.py
uv run python scripts/03_limitations.py
uv run python scripts/04_tools_and_toolnode.py
```

The first script currently contains commented-out alternatives showing direct OpenAI SDK, HTTP request, and LangChain calls. Uncomment the approach you want to try before running it. The later examples make model requests when run and may incur API usage charges.

The weather tool uses Open-Meteo's public geocoding and forecast APIs and does not require an API key. The tool example uses Gampaha in its sample question; change the question in `scripts/04_tools_and_toolnode.py` to try another place.

## Project layout

```text
.
|-- scripts/
|   |-- 00_providers_wrappers.py
|   |-- 01_chat_and_messages.py
|   |-- 02_temparature_and_top_p.py
|   |-- 03_limitations.py
|   |-- 04_tools_and_toolnode.py
|   |-- config.py
|   |-- corpus.py
|   `-- weather.py
|-- src/
|   `-- stem_link_rag/
|-- notebooks/
|-- pyproject.toml
`-- uv.lock
```

`scripts/config.py` centralizes model configuration and loads `.env`. The current model identifier is set there. The installable package entry point (`stem-link-rag`) is only a placeholder at this stage; the runnable learning examples are under `scripts/`.

## Development

The project dependencies are declared in `pyproject.toml`, with `uv.lock` recording the resolved environment. The `dev` dependency group includes Marimo for notebook-style development. To install development dependencies:

```powershell
uv sync --group dev
```

## Data and attribution

The sample rice cultivation facts identify the Sri Lanka Department of Agriculture's Rice Research and Development Institute (RRDI) or the Department of Agriculture (DOA) in their source labels. Consult the relevant agencies for authoritative, up-to-date recommendations before making field decisions.

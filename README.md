# AI Marketing Agent (Meta Ads Intelligence)

This is an ongoing  project where it is an AI-powered marketing analyst agent that interfaces with Meta (Facebook) Ads data to provide intelligent, 
conversational insights. It uses a LangGraph-based workflow and Anthropic Claude (via Amazon Bedrock) to answer complex business queries using live ad campaign data.

## Key Features

- **Conversational Analytics**: Ask natural-language questions like “Which audience performed best last quarter?” and get direct, contextual answers.
- **LangGraph-Powered Workflow**: The system uses a graph-based state machine to manage logic and data flow, ensuring modular and extendable behavior.
- **Document-Aware Reasoning**: The agent fetches relevant campaign documents or reports using a retriever before generating its answer.
- **LLM Integration**: Uses Claude v2 via Amazon Bedrock for natural-language understanding and generation.
- **Meta Ads Data Compatible**: Designed to work with Facebook Ads data—retrieving, summarizing, and analyzing campaign performance for marketing teams.

## How It Works

1. User inputs a marketing-related question.
2. The system uses a retriever to fetch related Meta Ads data (stored documents or vector embeddings).
3. A prompt is created: `"You're a marketing analyst. Answer using the data: {input}"`
4. Claude v2 processes the question and retrieved context to generate a natural-language response.
5. LangGraph orchestrates the flow from input to LLM output.

## Tech Stack

- **LangChain / LangGraph**
- **Amazon Bedrock (Claude v2)**
- **Python (TypedDict, dotenv)**
- **Custom Retriever for Meta Ads data**

##  Example Use Cases

- "Which campaign had the highest ROI in the last 30 days?"
- "Summarize ad performance for Product X targeting U.S. audiences."
- "List underperforming ad sets with budget over $500."



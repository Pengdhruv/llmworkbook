"""
Example usage script for Ollama API endpoint.
"""

import pandas as pd
from llmworkbook import LLMConfig, LLMRunner, LLMDataFrameIntegrator
from dotenv import load_dotenv

load_dotenv()


def main():
    # 1. Create a sample dataframe
    data = {
        "id": [1, 2, 3],
        "prompt_text": [
            "Explain Newton's first law in simple terms.",
            "Write a short poem about the moon.",
            "Give me 3 tips for better time management.",
        ],
    }
    df = pd.DataFrame(data)

    # 2. Create an LLM configuration
    config = LLMConfig(
        provider="gpt4all",
        system_prompt="Process these Data rows as per the provided prompt",
        options={
            "url": "http://localhost:4891",
            "model": "Mistral Instruct",
            "options": {"max_tokens": 50, "temperature": 0.28},
        },
    )

    # 3. Instantiate the runner and the integrator
    runner = LLMRunner(config)
    integrator = LLMDataFrameIntegrator(runner=runner, df=df)

    # 4. Add LLM responses to the df
    updated_df = integrator.add_llm_responses(
        prompt_column="prompt_text", response_column="llm_response", async_mode=True
    )

    print("DataFrame with LLM responses:\n", updated_df)


if __name__ == "__main__":
    main()

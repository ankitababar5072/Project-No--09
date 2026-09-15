# ============================================================
# LangChain + OpenAI Configuration
# ============================================================

import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


# Load environment variables from the .env file.
# This keeps API keys separate from the source code.
load_dotenv()


# Read the OpenAI API key from the environment.
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# Stop the application if the OpenAI API key is not configured.
if not OPENAI_API_KEY:
    raise ValueError(
        "OPENAI_API_KEY not found in .env file"
    )


# Initialize the LangChain ChatOpenAI model.
# temperature=0 makes the model output more consistent.
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


# Confirmation message used during configuration testing.
print(
    "LangChain + OpenAI configuration loaded successfully!"
)
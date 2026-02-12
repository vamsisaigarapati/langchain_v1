"""
init_chat_model Examples - Unified Model Initialization
========================================================
The init_chat_model function provides a unified interface to initialize
chat models from different providers (OpenAI, Groq, Google, Anthropic, etc.)
"""

import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

# Load environment variables
load_dotenv()

# =============================================================================
# Example 1: Initialize OpenAI Model
# =============================================================================
print("=" * 80)
print("Example 1: OpenAI Model")
print("=" * 80)

try:
    openai_model = init_chat_model(
        model="gpt-4",
        model_provider="openai",
        api_key=os.getenv("OPENAI_API_KEY"),
        temperature=0.7
    )
    print("✅ OpenAI model initialized successfully")
    print(f"Model: {openai_model}")
except Exception as e:
    print(f"❌ Error: {e}")

# =============================================================================
# Example 2: Initialize Groq Model
# =============================================================================
print("\n" + "=" * 80)
print("Example 2: Groq Model")
print("=" * 80)

groq_model = init_chat_model(
    model="llama-3.3-70b-versatile",
    model_provider="groq",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.7
)
print("✅ Groq model initialized successfully")
print(f"Model: {groq_model}")

# =============================================================================
# Example 3: Initialize Google Gemini Model
# =============================================================================
print("\n" + "=" * 80)
print("Example 3: Google Gemini Model")
print("=" * 80)

gemini_model = init_chat_model(
    model="gemini-2.5-flash",
    model_provider="google-genai",
    api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7
)
print("✅ Gemini model initialized successfully")
print(f"Model: {gemini_model}")

# =============================================================================
# Example 4: Auto-detect Provider (using model name)
# =============================================================================
print("\n" + "=" * 80)
print("Example 4: Auto-detect Provider")
print("=" * 80)

# LangChain can auto-detect the provider based on model name pattern
auto_model = init_chat_model(
    "groq/llama-3.1-8b-instant",  # Provider prefix in model name
    temperature=0.5
)
print("✅ Model initialized with auto-detection")
print(f"Model: {auto_model}")

# =============================================================================
# Example 5: Test Model with a Simple Prompt
# =============================================================================
print("\n" + "=" * 80)
print("Example 5: Test Groq Model with Prompt")
print("=" * 80)

response = groq_model.invoke("Say 'Hello, I am working!' in a cheerful way")
print("Model Response:")
print(response.content)

# =============================================================================
# Example 6: Different Models with Same Interface
# =============================================================================
print("\n" + "=" * 80)
print("Example 6: Comparing Different Models")
print("=" * 80)

models = {
    "Groq (Llama 3.3)": init_chat_model(
        "llama-3.3-70b-versatile",
        model_provider="groq",
        api_key=os.getenv("GROQ_API_KEY")
    ),
    "Gemini 2.5 Flash": init_chat_model(
        "gemini-2.5-flash",
        model_provider="google-genai",
        api_key=os.getenv("GOOGLE_API_KEY")
    )
}

prompt = "What is the capital of France? Answer in one word."

for model_name, model in models.items():
    print(f"\n{model_name}:")
    response = model.invoke(prompt)
    print(f"  → {response.content}")

# =============================================================================
# Example 7: Advanced Configuration
# =============================================================================
print("\n" + "=" * 80)
print("Example 7: Advanced Configuration")
print("=" * 80)

advanced_model = init_chat_model(
    model="llama-3.3-70b-versatile",
    model_provider="groq",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.8,
    max_tokens=1000,
    # streaming=True,  # Enable streaming
    # top_p=0.9,
)
print("✅ Advanced model configuration initialized")
print(f"Model: {advanced_model}")

print("\n" + "=" * 80)
print("All Examples Completed!")
print("=" * 80)

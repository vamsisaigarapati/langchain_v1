"""
Jupyter Notebook Examples for init_chat_model
==============================================
Copy these cells into your notebook for easy testing
"""

# =============================================================================
# CELL 1: Setup and Import
# =============================================================================
"""
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()
print("✅ Environment loaded successfully")
"""

# =============================================================================
# CELL 2: Initialize Groq Model (Recommended - Fast & Free)
# =============================================================================
"""
# Initialize Groq model using init_chat_model
groq_model = init_chat_model(
    model="llama-3.3-70b-versatile",
    model_provider="groq",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.7
)

print("✅ Groq model initialized")
print(f"Model type: {type(groq_model)}")

# Test it
response = groq_model.invoke("Hello! Introduce yourself in one sentence.")
print(f"\nResponse: {response.content}")
"""

# =============================================================================
# CELL 3: Initialize Google Gemini Model
# =============================================================================
"""
# Initialize Gemini model using init_chat_model
gemini_model = init_chat_model(
    model="gemini-2.5-flash",
    model_provider="google-genai",
    api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7
)

print("✅ Gemini model initialized")

# Test it
response = gemini_model.invoke("What's 25 * 47?")
print(f"Response: {response.content}")
"""

# =============================================================================
# CELL 4: Initialize OpenAI Model (if you have credits)
# =============================================================================
"""
# Initialize OpenAI model using init_chat_model
try:
    openai_model = init_chat_model(
        model="gpt-4o-mini",  # Cheaper model
        model_provider="openai",
        api_key=os.getenv("OPENAI_API_KEY"),
        temperature=0.7
    )
    
    print("✅ OpenAI model initialized")
    
    # Test it
    response = openai_model.invoke("Say hi!")
    print(f"Response: {response.content}")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("This is likely due to quota limits. Use Groq or Gemini instead.")
"""

# =============================================================================
# CELL 5: Compare Multiple Models
# =============================================================================
"""
# Compare responses from different models
question = "Explain quantum computing in one sentence."

models = {
    "Groq": init_chat_model("llama-3.3-70b-versatile", model_provider="groq"),
    "Gemini": init_chat_model("gemini-2.5-flash", model_provider="google-genai"),
}

print(f"Question: {question}\n")
for name, model in models.items():
    response = model.invoke(question)
    print(f"{name}: {response.content}\n")
"""

# =============================================================================
# CELL 6: Use with LangChain Agents
# =============================================================================
"""
from langchain.agents import create_agent

def get_quotes(name: str) -> str:
    '''get a romantic appreciation'''
    return f"Hey {name}, you are amazing!"

# Initialize model
llm = init_chat_model(
    "llama-3.3-70b-versatile",
    model_provider="groq",
    temperature=0.7
)

# Create agent
agent = create_agent(
    model=llm,
    tools=[get_quotes],
    system_prompt="You are a friendly assistant"
)

# Test agent
result = agent.invoke({
    "messages": [{"role": "user", "content": "My name is Vamsi"}]
})

print(result)
"""

# =============================================================================
# CELL 7: Auto-detect Model Provider (Advanced)
# =============================================================================
"""
# Using provider prefix in model name
auto_groq = init_chat_model("groq/llama-3.1-8b-instant")
auto_gemini = init_chat_model("google-genai/gemini-2.5-flash")

# Test auto-detected models
print("Auto Groq:", auto_groq.invoke("Hi!").content)
print("Auto Gemini:", auto_gemini.invoke("Hi!").content)
"""

# =============================================================================
# CELL 8: Streaming Responses (Advanced)
# =============================================================================
"""
# Initialize model with streaming
streaming_model = init_chat_model(
    "llama-3.3-70b-versatile",
    model_provider="groq",
    streaming=True
)

# Stream the response
print("Streaming response:")
for chunk in streaming_model.stream("Write a haiku about coding"):
    print(chunk.content, end="", flush=True)
print()
"""

print("\n" + "=" * 80)
print("Copy the code from each cell above into your Jupyter notebook!")
print("=" * 80)

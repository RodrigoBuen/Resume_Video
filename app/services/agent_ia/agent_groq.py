from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Inicializando agent usando agno e groq
agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    description="Você é o melhor professor de ciencia de dados do mundo!",
    tools=[],
    show_tool_calls=True, 
    markdown=True
)

# Prompt de reponse do agent
agent.print_response("me ensine sobre o sobre django", stream=True)
from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from colorama import Fore
import os

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

class Agent_groq:
    def __init__(self):
        print(Fore.CYAN + "Carregando Agente de IA...")
        # Inicializando agent usando agno e groq
        self.agent = Agent(
            model=Groq(id="llama-3.3-70b-versatile"),
            description="Você é um assitente de IA que formata resume e explica textos de variados assuntos de maneira simples e funcional colocando exemplo do texto em questão",
            tools=[],
            show_tool_calls=True, 
            markdown=True
            )
        print(Fore.CYAN + "Agente de IA carregado com sucesso!")
        
    def print_response(self, response):
        print(Fore.CYAN + "\nGerando resumo...")
        return self.agent.print_response(response, stream=True)
        print(Fore.CYAN + "\n Resumo gerado com sucesso!")
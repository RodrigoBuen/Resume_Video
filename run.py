from app.services.extractor.audio import Download_link
from colorama import Fore
from app.services.extractor.text import Extract_text
from app.services.agent_ia.agent_groq import Agent_groq

if __name__ == "__main__":
    print(Fore.CYAN + "🎵 Conversor de Áudio do YouTube → MP3")
    print(Fore.WHITE + "Digite a URL do vídeo abaixo:\n")

    url = input(Fore.YELLOW + "🔸 URL: ").strip()
    if url:
        downloader = Download_link(url)
        if downloader.nome_final:
            extract_text = Extract_text(downloader.nome_final)
            response = extract_text.audio_text()

            agent = Agent_groq()
            agent.print_response(response)
        else:
            print(Fore.RED + "❌ Erro ao baixar o áudio.")
    else:
        print(Fore.RED + "❌ Nenhuma URL fornecida.")
    
    

from time import sleep
from pytubefix import YouTube
from pytubefix.cli import on_progress
from moviepy import AudioFileClip
import os, shutil, re
from pathlib import Path
from colorama import init, Fore
import unicodedata

init(autoreset=True)

def limpar_nome(nome):
    """Remove caracteres especiais e normaliza o nome do arquivo"""
    nome = unicodedata.normalize('NFKD', nome).encode('ASCII', 'ignore').decode('ASCII')
    nome = re.sub(r'[^\w\s-]', '', nome).strip()
    nome = re.sub(r'[-\s]+', '_', nome)
    return nome

pasta_atual = Path(".").resolve()
nome_limpo = None  # Variável no nível do módulo

class Download_link():
    def __init__(self, url):
        self.video_url = url
        self.nome_final = self.run()
        if self.nome_final:
            self.move_create()

    def run(self):
        try:
            print(Fore.CYAN + "🔗 Conectando ao YouTube...")
            self.url_extractor = YouTube(self.video_url, on_progress_callback=on_progress)

            print(Fore.YELLOW + f"\n🎬 Título: {self.url_extractor.title}")

            nome_limpo = limpar_nome(self.url_extractor.title)
            self.nome_final = nome_limpo

            print(Fore.BLUE + "\n⬇️ Baixando áudio...")
            self.ys = self.url_extractor.streams.get_audio_only()
            self.ys.download(filename=f"{nome_limpo}.m4a")
            print(Fore.GREEN + "✅ Download concluído")

            print(Fore.BLUE + "\n🎧 Convertendo para MP3...")
            self.audio_a4 = AudioFileClip(f"{nome_limpo}.m4a")
            self.audio_a4.write_audiofile(f"{nome_limpo}.mp3")
            print(Fore.GREEN + "✅ Conversão finalizada")

            os.remove(f"{pasta_atual}/{nome_limpo}.m4a")
            print(Fore.MAGENTA + "🗑️ Arquivo temporário removido")
            return nome_limpo

        except Exception as e:
            print(Fore.RED + f"\n❌ Erro durante o processo: {e}")
            return None

    def move_create(self):
        try:
            destino = pasta_atual / "Musicas"
            destino.mkdir(exist_ok=True)

            origem = f"{pasta_atual}/{self.nome_final}.mp3"
            destino_final = f"{destino}/{self.nome_final}.mp3"
            shutil.move(origem, destino_final)

            print(Fore.GREEN + f"\n📁 Arquivo movido para: {destino_final}")
        except Exception as e:
            print(Fore.RED + f"\n❌ Erro ao mover o arquivo: {e}")
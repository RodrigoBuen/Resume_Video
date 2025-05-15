import torch
import whisper
from app.services.extractor.audio import pasta_atual
from colorama import Fore


class Extract_text:
    def __init__(self, nome_arquivo):
        print(Fore.CYAN + "Carregando modelo de extração de texto...")
        self.modelo = whisper.load_model("base")
        self.nome_arquivo = nome_arquivo

    def audio_text(self):
        print("Device:", "cuda" if torch.cuda.is_available() else "cpu")
        audio = f"{pasta_atual}/Musicas/{self.nome_arquivo}.mp3"
        print(Fore.CYAN + "Extraindo texto...")
        result = self.modelo.transcribe(audio)
        print(Fore.GREEN + "Texto extraído com sucesso!")
        return result["text"]

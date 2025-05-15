# 🎵 Resume Video

## 📝 Resumo

O Resume Video é uma ferramenta poderosa que combina tecnologias de IA para transformar conteúdo de áudio em insights valiosos. O projeto nasceu da necessidade de extrair e compreender informações de vídeos do YouTube de forma eficiente, permitindo que usuários obtenham resumos inteligentes do conteúdo sem precisar assistir ao vídeo inteiro.

## 💡 Motivação

A motivação principal para o desenvolvimento deste projeto foi a crescente quantidade de conteúdo em vídeo disponível online e a necessidade de consumir esse conteúdo de forma mais eficiente. Muitas vezes, assistir a um vídeo completo pode ser demorado, e nem sempre temos tempo para isso. Além disso, a extração de informações-chave de vídeos pode ser útil para:

- Pesquisadores que precisam analisar conteúdo em vídeo
- Estudantes que buscam resumos de aulas ou palestras
- Profissionais que precisam extrair insights de vídeos de treinamento
- Qualquer pessoa que queira consumir conteúdo de forma mais eficiente

O projeto também serve como uma demonstração prática de como diferentes tecnologias de IA podem ser combinadas para criar soluções úteis e inovadoras.

## ✨ Funcionalidades

- Download de áudio de vídeos do YouTube
- Conversão automática para MP3
- Extração de texto do áudio usando Whisper AI
- Geração de resumo inteligente usando Groq AI
- Interface amigável com feedback visual colorido

## 🚀 Requisitos

- Python 3.8 ou superior
- FFmpeg instalado no sistema
- Conta na Groq AI (para a chave de API)

## 📦 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/Resume_Video.git
cd Resume_Video
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
Crie um arquivo `.env` na raiz do projeto e adicione sua chave API da Groq:
```
GROQ_API_KEY=sua_chave_api_aqui
```

## 🎯 Como Usar

1. Execute o script principal:
```bash
python run.py
```

2. Cole a URL do vídeo do YouTube quando solicitado

3. Aguarde o processo:
   - Download do áudio
   - Conversão para MP3
   - Extração do texto
   - Geração do resumo

4. O arquivo de áudio será salvo na pasta `Musicas`

## 🛠️ Tecnologias Utilizadas

- [pytubefix](https://github.com/pytube/pytube) - Para download de vídeos do YouTube
- [moviepy](https://zulko.github.io/moviepy/) - Para manipulação de áudio
- [whisper](https://github.com/openai/whisper) - Para transcrição de áudio
- [Groq](https://groq.com/) - Para processamento de linguagem natural
- [colorama](https://pypi.org/project/colorama/) - Para formatação colorida no terminal

## 📁 Estrutura do Projeto

```
Resume_Video/
├── app/
│   ├── services/
│   │   ├── extractor/
│   │   │   ├── audio.py
│   │   │   └── text.py
│   │   └── agent_ia/
│   │       └── agent_groq.py
├── Musicas/
├── .env
├── requirements.txt
├── run.py
└── README.md
```

## ⚠️ Limitações

- Requer conexão com a internet
- Necessita de FFmpeg instalado
- Processamento de áudio pode ser lento dependendo do tamanho do arquivo
- Requer chave API da Groq

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👥 Autores

- Rodrigo Bueno - Desenvolvimento inicial

## 🙏 Agradecimentos

- OpenAI pelo modelo Whisper
- Groq pela API de processamento de linguagem natural
- Comunidade Python por todas as bibliotecas incríveis

-----------------------------------------------------------------------------------------------------------------------------------

# 🎵 Resume Video

## 📝 Summary

Resume Video is a powerful tool that combines AI technologies to transform audio content into valuable insights. The project was born from the need to efficiently extract and understand information from YouTube videos, allowing users to obtain intelligent summaries of the content without having to watch the entire video.

## 💡 Motivation

The main motivation for developing this project was the growing amount of video content available online and the need to consume this content more efficiently. Often, watching a complete video can be time-consuming, and we don't always have time for it. Additionally, extracting key information from videos can be useful for:

- Researchers who need to analyze video content
- Students looking for summaries of lectures or talks
- Professionals who need to extract insights from training videos
- Anyone who wants to consume content more efficiently

The project also serves as a practical demonstration of how different AI technologies can be combined to create useful and innovative solutions.

## ✨ Features

- YouTube video audio download
- Automatic MP3 conversion
- Audio text extraction using Whisper AI
- Intelligent summary generation using Groq AI
- User-friendly interface with colored visual feedback

## 🚀 Requirements

- Python 3.8 or higher
- FFmpeg installed on the system
- Groq AI account (for API key)

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/seu-usuario/Resume_Video.git
cd Resume_Video
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
Create a `.env` file in the project root and add your Groq API key:
```
GROQ_API_KEY=your_api_key_here
```

## 🎯 How to Use

1. Run the main script:
```bash
python run.py
```

2. Paste the YouTube video URL when prompted

3. Wait for the process:
   - Audio download
   - MP3 conversion
   - Text extraction
   - Summary generation

4. The audio file will be saved in the `Musicas` folder

## 🛠️ Technologies Used

- [pytubefix](https://github.com/pytube/pytube) - For YouTube video downloads
- [moviepy](https://zulko.github.io/moviepy/) - For audio manipulation
- [whisper](https://github.com/openai/whisper) - For audio transcription
- [Groq](https://groq.com/) - For natural language processing
- [colorama](https://pypi.org/project/colorama/) - For terminal color formatting

## 📁 Project Structure

```
Resume_Video/
├── app/
│   ├── services/
│   │   ├── extractor/
│   │   │   ├── audio.py
│   │   │   └── text.py
│   │   └── agent_ia/
│   │       └── agent_groq.py
├── Musicas/
├── .env
├── requirements.txt
├── run.py
└── README.md
```

## ⚠️ Limitations

- Requires internet connection
- Needs FFmpeg installed
- Audio processing can be slow depending on file size
- Requires Groq API key

## 📝 License

This project is under the MIT license. See the [LICENSE](LICENSE) file for more details.

## 👥 Authors

- Rodrigo Bueno - Initial development

## 🙏 Acknowledgments

- OpenAI for the Whisper model
- Groq for the natural language processing API
- Python community for all the amazing libraries 
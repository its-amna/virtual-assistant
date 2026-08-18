# virtual-assistant
A Python-based virtual assistant using Groq API and text-to-speech.

# 🤖 Jarvis - AI-Powered Voice Assistant

An intelligent, Python-based virtual assistant that listens for a wake word, processes custom commands, fetches live news, plays music, opens web applications, and leverages **Groq Cloud AI (Llama 3.1)** for conversational intelligence.

---

## ✨ Features

- 🎙️ **Voice Recognition:** Listens to real-time voice input using your system microphone.
- ⚡ **Groq AI Integration:** Powered by Llama 3.1 (`llama-3.1-8b-instant`) for fast and concise answers.
- 🔊 **Text-to-Speech (TTS):** Uses `gTTS` and `pygame` for clear, natural audio feedback.
- 🌐 **Web Automation:** Automatically opens websites like Google, YouTube, and Facebook.
- 🎵 **Music Playback:** Integrates a local music library to launch custom tracks/links.
- 📰 **Live News Headlines:** Fetches real-time general news top headlines without extra setup.
- 🔒 **Secure Environment:** Manages sensitive keys safely using environment variables (`.env`).

---

## 🛠️ Tech Stack & Libraries

- **Language:** Python 3.x
- **AI Engine:** Groq API (Llama 3.1 Model)
- **Speech Recognition:** `SpeechRecognition`
- **Text-to-Speech:** `gTTS` (Google Text-to-Speech) & `pygame` (Audio Player)
- **HTTP Requests:** `requests`
- **Environment Management:** `python-dotenv`

---

## 🚀 Getting Started

### 1. Prerequisites
Make sure you have Python 3.8 or higher installed on your computer.

### 2. Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/its-amna/virtual-assistant.git](https://github.com/its-amna/virtual-assistant.git)
   cd virtual-assistant


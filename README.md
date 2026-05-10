# 🧠 Chatbot with Memory

> Day 3 of my AI Engineering Journey — Built a chatbot that 
> actually remembers what you said.

---

## 💭 The Problem I Solved

Most basic chatbots are goldfish 🐟

Every time you send a new message they forget everything —
your name, what you discussed, the full context.

This project fixes that completely.

---

## 💡 How Memory Actually Works

This is the key insight of this project:

Every time you send a message, the entire conversation
history is passed to the AI — not just your latest message.

Message 1: You say "My name is Prashik"

Message 2: You ask "What is my name?"

Without memory → AI has no idea

With memory    → AI says "Your name is Prashik"

This is exactly how ChatGPT remembers your conversations.
No magic. Just passing history.

---

## ✨ Features

- 🧠 **Full conversation memory** — remembers everything said
- 🎭 **3 built-in personas** — Research Assistant, Career Coach, Python Tutor
- ✨ **Custom persona** — create your own AI character from scratch
- 📜 **History command** — view full conversation anytime
- 🔄 **Clear command** — reset memory and start fresh
- 💾 **Memory counter** — shows how many messages are in context
- 🎨 **Colored terminal UI** — clean and visual experience

---

## 🎭 Available Personas

| Persona | Role | Best For |
|---------|------|---------|
| 🔬 Alex | Research Assistant | Studying, learning, explaining concepts |
| 💼 Zara | Career Coach | Resume, interviews, career advice |
| 🐍 Max | Python Tutor | Coding help, debugging, learning Python |
| ✨ Custom | Your creation | Anything you want |

---

## 🔑 The Core Concept — Conversation History

```python
# This list IS the memory
conversation_history = [
    {"role": "system", "content": "You are Alex..."},  # Persona
    {"role": "user", "content": "My name is Prashik"}, # User message
    {"role": "assistant", "content": "Nice to meet you Prashik!"}, # AI reply
    {"role": "user", "content": "What is my name?"},   # New message
    # Full history sent every time → AI remembers
]
```

---

## ⚙️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| Groq API | AI inference platform |
| LLaMA 3.3 70B | The underlying language model |
| python-dotenv | Secure API key management |
| VS Code | Development environment |
| Git & GitHub | Version control |

---

## 🚀 How to Run

1. Clone the repository
```bash
   git clone https://github.com/PrashikSawant/chatbot-with-memory.git
   cd chatbot-with-memory
```

2. Install dependencies
```bash
   pip install groq python-dotenv
```

3. Create a `.env` file
```bash
  GROQ_API_KEY=your-key-here
```

4. Run the app
```bash
   python main.py
```

5. Choose a persona and start chatting!

---

## 💬 Commands

| Command | What It Does |
|---------|-------------|
| `history` | Shows full conversation so far |
| `clear` | Resets memory, starts fresh |
| `quit` | Exits the chatbot |

---

## 📚 What I Learned

- AI has no memory by default — you have to build it
- Memory = passing full conversation history with every API call
- System prompts define the entire personality of an AI
- The same model behaves completely differently with different instructions
- How to build a structured multi-feature terminal application

---

## 🗺️ What's Next

- 🔜 RAG powered Document Q&A System
- 🔜 AI Agent with web search capability
- 🔜 Full stack web app with Streamlit

---

## 👨‍💻 About Me

I am Prashik — an aspiring AI Engineer on a 4-month intensive
journey to become job-ready in Generative AI Engineering.

Follow my journey → [LinkedIn](https://www.linkedin.com/in/prashik-sawant-ds)
See all projects → [GitHub](https://github.com/PrashikSawant)

---

*Day 3 of 120 | May 11, 2026 | Status: ✅ Complete*

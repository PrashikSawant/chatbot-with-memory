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

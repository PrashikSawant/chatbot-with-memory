from groq import Groq
from dotenv import load_dotenv
import os
import time
from datetime import datetime

load_dotenv()
client = Groq(api_key=os.getenv("Groq_API_KEY"))

# Adding Colours

GREEN  = "\033[92m"
BLUE   = "\033[94m"
CYAN   = "\033[96m"
YELLOW = "\033[93m"
RED    = "\033[91m"
BOLD   = "\033[1m"
RESET  = "\033[0m"
DIM    = "\033[2m"
PURPLE = "\033[95m"

#AI call with full history
def ask_ai(conversation_history):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=conversation_history
    )
    return response.choices[0].message.content

# ── STREAMING PRINT ───────────────────────────────────────────────────────────
def stream_print(text, color=GREEN):
    words = text.split()
    for word in words:
        print(f"{color}{word}{RESET}", end=' ', flush=True)
        time.sleep(0.03)
    print()

# ── PRINT HEADER ──────────────────────────────────────────────────────────────
def print_header(persona_name, persona_role):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n{BOLD}{CYAN}{'='*55}{RESET}")
    print(f"{BOLD}{CYAN}   🧠  Chatbot with Memory{RESET}")
    print(f"{BOLD}{CYAN}   Persona : {persona_name} — {persona_role}{RESET}")
    print(f"{BOLD}{CYAN}   Powered by LLaMA 3.3 70B via Groq{RESET}")
    print(f"{BOLD}{CYAN}{'='*55}{RESET}\n")
    print(f"{DIM}   Type 'quit' to exit | 'history' to see chat | 'clear' to reset memory{RESET}\n")

# ── SHOW HISTORY ──────────────────────────────────────────────────────────────
def show_history(conversation_history):
    print(f"\n{BOLD}{YELLOW}── Conversation History ──────────────────────────{RESET}\n")
    # Skip system message at index 0
    for msg in conversation_history[1:]:
        if msg["role"] == "user":
            print(f"{BOLD}{BLUE}You:{RESET} {msg['content']}")
        else:
            print(f"{BOLD}{GREEN}AI: {RESET} {msg['content']}")
        print()
    print(f"{DIM}{'─'*55}{RESET}\n")

# ── CHOOSE PERSONA ────────────────────────────────────────────────────────────
def choose_persona():
    personas = {
        "1": {
            "name": "Alex",
            "role": "Research Assistant",
            "system": "You are Alex, a brilliant research assistant. You help with academic topics, summarize papers, explain complex concepts clearly, and remember everything discussed in the conversation. You are curious, precise, and encouraging."
        },
        "2": {
            "name": "Zara",
            "role": "Career Coach",
            "system": "You are Zara, an experienced career coach specializing in tech careers and AI engineering. You give actionable advice, help with resumes, interview prep, and career planning. You are motivating, practical, and direct."
        },
        "3": {
            "name": "Max",
            "role": "Python Tutor",
            "system": "You are Max, an expert Python and AI programming tutor. You explain code clearly, debug problems patiently, give examples, and remember what the student has learned so far. You are patient, clear, and encouraging."
        },
        "4": {
            "name": "Custom",
            "role": "Your Own Persona",
            "system": None
        }
    }

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n{BOLD}{CYAN}{'='*55}{RESET}")
    print(f"{BOLD}{CYAN}   🧠  Chatbot with Memory — Persona Select{RESET}")
    print(f"{BOLD}{CYAN}{'='*55}{RESET}\n")
    print(f"{BOLD}Choose your AI persona:\n{RESET}")
    print(f"  {GREEN}{BOLD}1.{RESET} 🔬 Alex      — Research Assistant")
    print(f"  {BLUE}{BOLD}2.{RESET} 💼 Zara      — Career Coach")
    print(f"  {YELLOW}{BOLD}3.{RESET} 🐍 Max       — Python Tutor")
    print(f"  {PURPLE}{BOLD}4.{RESET} ✨ Custom    — Create your own\n")

    choice = input(f"{BOLD}Enter choice (1-4): {RESET}").strip()

    if choice not in personas:
        choice = "1"

    persona = personas[choice]

    if choice == "4":
        print(f"\n{BOLD}Enter persona name: {RESET}", end="")
        persona["name"] = input().strip() or "AI"
        print(f"{BOLD}Enter persona role: {RESET}", end="")
        persona["role"] = input().strip() or "Assistant"
        print(f"{BOLD}Describe how this persona should behave: {RESET}", end="")
        custom_system = input().strip()
        persona["system"] = f"You are {persona['name']}, a {persona['role']}. {custom_system}. Remember everything discussed in the conversation."

    return persona

# ── MAIN ──────────────────────────────────────────────────────────────────────
def main():
    # Choose persona
    persona = choose_persona()

    # Initialize conversation history with system prompt
    conversation_history = [
        {"role": "system", "content": persona["system"]}
    ]

    print_header(persona["name"], persona["role"])
    print(f"{GREEN}✅ {persona['name']} is ready! Start chatting.{RESET}\n")

    message_count = 0

    while True:
        # Get user input
        user_input = input(f"{BOLD}{BLUE}You: {RESET}").strip()

        # Commands
        if user_input.lower() == "quit":
            print(f"\n{GREEN}👋 Goodbye! Your conversation had {message_count} messages.{RESET}\n")
            break

        if user_input.lower() == "history":
            show_history(conversation_history)
            continue

        if user_input.lower() == "clear":
            conversation_history = [
                {"role": "system", "content": persona["system"]}
            ]
            message_count = 0
            print(f"\n{YELLOW}🔄 Memory cleared. Starting fresh.{RESET}\n")
            continue

        if user_input == "":
            continue

        # Add user message to history
        conversation_history.append({
            "role": "user",
            "content": user_input
        })

        # Loading
        print(f"\n{YELLOW}⏳ {persona['name']} is thinking...", end='', flush=True)
        for _ in range(3):
            time.sleep(0.3)
            print(".", end='', flush=True)
        print(f"{RESET}\n")

        # Get AI response
        ai_response = ask_ai(conversation_history)

        # Add AI response to history — THIS IS THE MEMORY
        conversation_history.append({
            "role": "assistant",
            "content": ai_response
        })

        message_count += 1

        # Print response
        print(f"{BOLD}{GREEN}{persona['name']}: {RESET}", end='')
        stream_print(ai_response, GREEN)

        # Show memory indicator
        total_messages = len(conversation_history) - 1
        print(f"\n{DIM}   💾 Memory: {total_messages} messages in context{RESET}\n")
        print(f"{DIM}{'─'*55}{RESET}\n")

if __name__ == "__main__":
    main()
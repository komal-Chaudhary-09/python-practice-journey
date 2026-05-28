import random
import time

intents = {
    "greeting": [
        "Hey there! 👋 I'm PyBot.",
        "Hello! How can I help?",
        "Hi! Nice to chat with you.",
    ],

    "farewell": [
        "Goodbye! 👋",
        "See you later!",
        "Bye! Take care 😊",
    ],

    "how_are_you": [
        "I'm doing great! 😄",
        "All systems running perfectly 🤖",
        "I'm good! What about you?",
    ],

    "bot_name": [
        "I'm PyBot 🐍",
        "You can call me PyBot!",
        "My name is PyBot.",
    ],

    "python": [
        "Python is a very powerful language 🐍",
        "Python is beginner-friendly and amazing!",
        "Python is used in AI, web dev, and more.",
    ],

    "help": [
        "Try asking about Python or say hello!",
        "I can chat and answer simple questions.",
        "You can also ask me for jokes 😄",
    ],

    "joke": [
        "Why do programmers hate bugs? Because they bug them 😂",
        "Why was the computer cold? It forgot to close windows 🪟",
        "Python programmers don't byte, they hiss 🐍",
    ],

    "thanks": [
        "You're welcome 😊",
        "Anytime!",
        "Happy to help!",
    ],

    "default": [
        "I don't understand that yet.",
        "Can you rephrase that?",
        "Interesting... tell me more.",
    ]
}

keyword_map = {
    "hi": "greeting",
    "hello": "greeting",
    "hey": "greeting",

    "bye": "farewell",
    "goodbye": "farewell",

    "how are you": "how_are_you",

    "your name": "bot_name",
    "who are you": "bot_name",

    "python": "python",
    "coding": "python",
    "programming": "python",

    "help": "help",

    "joke": "joke",
    "funny": "joke",

    "thanks": "thanks",
    "thank you": "thanks",
}

memory = {
    "name": None,
    "message_count": 0,
}


def get_bot_reply(user_message):
    cleaned_message = user_message.lower().strip()

    if "my name is" in cleaned_message:
        name = cleaned_message.split("my name is")[1].strip().capitalize()
        memory["name"] = name
        return f"Nice to meet you, {name}! 😊"

    for keyword, intent in keyword_map.items():
        if keyword in cleaned_message:
            return random.choice(intents[intent])

    return random.choice(intents["default"])


def run_chatbot():
    print("\n🤖 PyBot Started! Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if not user_input.strip():
            continue

        memory["message_count"] += 1

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("PyBot: Goodbye 👋")
            break

        reply = get_bot_reply(user_input)

        time.sleep(0.5)
        print(f"PyBot: {reply}\n")


if __name__ == "__main__":
    run_chatbot()
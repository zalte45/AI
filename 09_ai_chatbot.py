"""Practical 9: Rule-based Artificial Intelligence chatbot.

This is a simple keyword/rule chatbot, not a trained AI model. It responds to
messages about greetings, AI, machine learning, Python, date, time, thanks,
and goodbye. Random choice selects between predefined responses.

Run: python 09_ai_chatbot.py
Type 'bye', 'goodbye', 'exit', or 'quit' to end the conversation.
"""

import re
import random
from datetime import datetime

# Possible responses for each supported topic.
responses = {
    "greeting": [
        "Hello! How can I help you?",
        "Hi! Nice to meet you.",
        "Hello! Ask me something about AI.",
    ],
    "ai": [
        "AI stands for Artificial Intelligence.",
        "AI enables computers to perform tasks requiring human intelligence.",
    ],
    "ml": [
        "Machine Learning is a branch of AI that learns from data.",
        "ML uses data and algorithms to make predictions.",
    ],
    "python": [
        "Python is a popular programming language.",
        "Python is widely used in AI and Machine Learning.",
    ],
    "thanks": [
        "You are welcome!",
        "Glad I could help!",
        "My pleasure!",
    ],
    "goodbye": [
        "Goodbye! Have a nice day.",
        "Thank you for chatting with me.",
        "See you again!",
    ],
}


def get_response(user_input):
    """Match the user's message against supported keyword patterns."""
    text = user_input.lower()

    if re.search(r"\b(hello|hi|hey|hii)\b", text):
        return random.choice(responses["greeting"])
    if re.search(r"\b(ai|artificial intelligence)\b", text):
        return random.choice(responses["ai"])
    if re.search(r"\b(ml|machine learning)\b", text):
        return random.choice(responses["ml"])
    if re.search(r"\b(python|programming)\b", text):
        return random.choice(responses["python"])
    if re.search(r"\b(date|today)\b", text):
        return "Today's date is " + datetime.now().strftime("%d-%m-%Y")
    if re.search(r"\b(time|current time)\b", text):
        return "Current time is " + datetime.now().strftime("%I:%M %p")
    if re.search(r"\b(thanks|thank you|thank)\b", text):
        return random.choice(responses["thanks"])
    if re.search(r"\b(bye|goodbye|exit|quit)\b", text):
        return random.choice(responses["goodbye"])

    return (
        "Sorry, I could not understand your question. "
        "Ask me about AI, ML, Python, date or time."
    )


def chatbot():
    """Run the conversation loop until the user enters an exit keyword."""
    print("=" * 50)
    print(" ARTIFICIAL INTELLIGENCE CHATBOT")
    print("=" * 50)
    print("Bot: Hello! I am your AI Chatbot.")
    print("Bot: Ask me about AI, ML, Python, date or time.")
    print("Bot: Type 'bye' or 'exit' to end the conversation.\n")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Bot:", response)
        if re.search(r"\b(bye|goodbye|exit|quit)\b", user_input.lower()):
            break


if __name__ == "__main__":
    chatbot()

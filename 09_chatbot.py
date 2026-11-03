import re
import random
from datetime import datetime

# Dictionary containing chatbot responses
responses = {

    # Responses for greeting
    "greeting": [
        "Hello! How can I help you?",
        "Hi! Nice to meet you.",
        "Hello! Ask me something about Artificial Intelligence."
    ],

    # Responses about Artificial Intelligence
    "ai": [
        "AI stands for Artificial Intelligence.",
        "Artificial Intelligence enables computers to perform tasks that normally require human intelligence."
    ],

    # Responses about Machine Learning
    "ml": [
        "Machine Learning is a branch of AI that allows computers to learn from data.",
        "ML uses data and algorithms to make predictions or decisions."
    ],

    # Responses about Python
    "python": [
        "Python is a popular programming language used in Artificial Intelligence.",
        "Python provides libraries such as NumPy, Pandas and Scikit-learn for AI and ML."
    ],

    # Responses for thanking
    "thanks": [
        "You are welcome!",
        "Glad I could help!",
        "My pleasure!"
    ],

    # Responses for goodbye
    "goodbye": [
        "Goodbye! Have a nice day.",
        "Thank you for chatting with me.",
        "See you again!"
    ]
}


# Function to find chatbot response
def get_response(user_input):

    # Convert user input into lowercase
    text = user_input.lower()

    # Check greeting pattern using regular expression
    if re.search(r"\b(hello|hi|hey|hii)\b", text):
        return random.choice(responses["greeting"])

    # Check Artificial Intelligence pattern
    elif re.search(r"\b(ai|artificial intelligence)\b", text):
        return random.choice(responses["ai"])

    # Check Machine Learning pattern
    elif re.search(r"\b(ml|machine learning)\b", text):
        return random.choice(responses["ml"])

    # Check Python or programming pattern
    elif re.search(r"\b(python|programming)\b", text):
        return random.choice(responses["python"])

    # Check date pattern and return today's date
    elif re.search(r"\b(date|today)\b", text):
        return "Today's date is " + datetime.now().strftime("%d-%m-%Y")

    # Check time pattern and return current time
    elif re.search(r"\b(time|current time)\b", text):
        return "Current time is " + datetime.now().strftime("%I:%M %p")

    # Check thank you pattern
    elif re.search(r"\b(thanks|thank you|thank)\b", text):
        return random.choice(responses["thanks"])

    # Check goodbye pattern
    elif re.search(r"\b(bye|goodbye|exit|quit)\b", text):
        return random.choice(responses["goodbye"])

    # Return default response if no pattern matches
    else:
        return (
            "Sorry, I could not understand your question. "
            "Please ask me about AI, ML, Python, date or time."
        )


# Main chatbot function
def chatbot():

    # Display chatbot heading
    print("=" * 50)
    print("        ARTIFICIAL INTELLIGENCE CHATBOT")
    print("=" * 50)

    # Display welcome messages
    print("Bot: Hello! I am your AI Chatbot.")
    print("Bot: You can ask me about AI, ML, Python, date or time.")
    print("Bot: Type 'bye' or 'exit' to end the conversation.")
    print()

    # Run chatbot continuously
    while True:

        # Take input from the user
        user_input = input("You: ")

        # Check whether the user wants to exit
        if re.search(r"\b(bye|goodbye|exit|quit)\b",
                     user_input.lower()):

            # Display goodbye response
            print("Bot:", get_response(user_input))

            # Stop the chatbot
            break

        # Get response from chatbot
        response = get_response(user_input)

        # Display chatbot response
        print("Bot:", response)


# Execute chatbot when the program runs directly
if __name__ == "__main__":
    chatbot()


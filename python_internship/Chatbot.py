import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]),
    (r"how are you", ["I'm good, thank you!", "I'm doing well."]),
    (r"what is your name", ["I'm a chatbot.", "You can call me ChatGPT."]),
    (r"quit|exit", ["Goodbye!", "See you later!"]),
    # Add more patterns and responses as needed
]

# Create a chatbot
chatbot = Chat(pairs, reflections)

def run_chatbot():
    print("Hello! I'm a simple chatbot. You can type 'quit' or 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit']:
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    nltk.download("punkt")  # Download the NLTK data needed for tokenization
    run_chatbot()

print("🤖 Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    # Greetings
    if user_input == "hello" or user_input == "hi":
        print("🤖 Chatbot: Hi there!")

    # Asking name
    elif user_input == "what is your name":
        print("🤖 Chatbot: I am your AI chatbot 🤖")

    # Asking help
    elif user_input == "help":
        print("🤖 Chatbot: I can chat with you. Try saying hello!")

    # Exit condition
    elif user_input == "bye":
        print("🤖 Chatbot: Goodbye! 👋")
        break

    # Default response
    else:
        print("🤖 Chatbot: Sorry, I don't understand that.")
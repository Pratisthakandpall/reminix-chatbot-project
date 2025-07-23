from langchain_community.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
import os
from dotenv import load_dotenv



load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


llm = ChatOpenAI(openai_api_key=api_key, temperature=0.7)
memory = ConversationBufferMemory()

conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

print(" Chatbot is ready! Type 'exit' to stop chatting.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Chatbot: Goodbye!")
        break

    response = conversation.predict(input=user_input)
    print("Bot:", response)


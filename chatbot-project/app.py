from dotenv import load_dotenv
import os
from langchain.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain


load_dotenv()


api_key = os.getenv("AZURE_OPENAI_API_KEY")
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")


os.environ["AZURE_OPENAI_API_KEY"] = api_key
os.environ["AZURE_OPENAI_ENDPOINT"] = endpoint
os.environ["AZURE_OPENAI_API_VERSION"] = api_version


llm = AzureChatOpenAI(
    deployment_name=deployment_name,
    openai_api_version=api_version,
)


memory = ConversationBufferMemory()


conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)


while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    response = conversation.predict(input=user_input)
    print("Bot:", response)
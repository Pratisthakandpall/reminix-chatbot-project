from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage
import os
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
CORS(app)


llm = AzureChatOpenAI(
    openai_api_base=os.getenv("AZURE_OPENAI_ENDPOINT"),
    openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    model=os.getenv("AZURE_OPENAI_MODEL"),
    openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message")

        if not user_message:
            return jsonify({"response": "No message received!"}), 400

        # Use LangChain to generate reply
        response = llm([HumanMessage(content=user_message)])
        return jsonify({"response": response.content})

    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

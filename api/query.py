from flask import Flask, request, jsonify
import requests
from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import LLMChain

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/query', methods=['POST'])
def api_call():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    user_question = data.get("question", "What is the project about?")

    url = "https://general-runtime.voiceflow.com/knowledge-base/query"
    payload = {
        "question": user_question,
        "chunkLimit": 2,
        "synthesis": True,
        "settings": {
            "model":
            "claude-instant-v1",
            "temperature":
            0.1,
            "system":
            "You are an AI FAQ assistant. Information will be provided to help answer the user's questions. Always summarize your response to be as brief as possible and be extremely concise. Your responses should be fewer than a couple of sentences. Do not reference the material provided in your response."
        }
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": ""
    }

    response = requests.post(url, json=payload, headers=headers)
    api_response = response.json()

    # Extract content and format it
    formatted_content = []
    for index, chunk in enumerate(api_response['chunks'], start=1):
        content = chunk['content']
        formatted_content.append(f"Reference {index}: {content}")

    # Define the prompt template
    prompt = PromptTemplate(
        input_variables=["formatted_content", "user_question"],
        template='''Based on this reference below: 

        {formatted_content}

        Answer the user question: {user_question}.

        Make sure to only answer the user's question and don't overwhelm them with too much information.
        ''')

    chatopenai = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        openai_api_key="")
    llmchain_chat = LLMChain(llm=chatopenai, prompt=prompt)
    answer = llmchain_chat.invoke({
        "formatted_content": formatted_content,
        "user_question": user_question
    })
    answer = answer['text']

    return jsonify({"answer": answer})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

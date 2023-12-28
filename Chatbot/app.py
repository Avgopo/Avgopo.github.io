from flask import Flask,redirect, render_template, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = "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"

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")

@app.route("/contacts")
def contacts():
    return render_template("contacts.html")

@app.route("/chatbot", methods=["GET","POST"])
def get_chat():
    user_input = request.json
    input = user_input["user_input_value"]
    chat_messages = [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': input}]
    response = jsonify(get_openai_response(chat_messages))
    return response

def get_openai_response(messages):
    response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages= messages
    )
    return response["choices"][0]["message"]['content']

if __name__ == "__main__":
    app.run(debug=True)

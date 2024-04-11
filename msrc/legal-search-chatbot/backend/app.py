from flask import Flask, request, jsonify
from flask_cors import CORS
from models import search, build_output, generate_chat_response

app = Flask(__name__)
CORS(app)

@app.route('/api/chat', methods=['POST'])
def chat_api():
    data = request.get_json()
    user_input = data['userInput']
    chat_history = data['chatHistory']

    search_results = search(user_input)
    search_output = build_output(search_results, user_input)

    bot_response = generate_chat_response(user_input, chat_history, search_output)

    return jsonify({'botResponse': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
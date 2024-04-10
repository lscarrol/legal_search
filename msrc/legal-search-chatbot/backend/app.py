from flask import Flask, request, jsonify
from flask_cors import CORS
from models import search, build_output

app = Flask(__name__)
CORS(app)

@app.route('/api/search', methods=['POST'])
def search_api():
    data = request.get_json()
    query = data['query']
    results = search(query)
    output = build_output(results, query)
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)
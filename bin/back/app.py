from flask import Flask, render_template, request
from models import search, build_output

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        query = request.form['query']
        results = search(query)
        output = build_output(results, query)
        return render_template('results.html', query=query, output=output)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
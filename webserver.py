# Flask webserver to run on localhost:5000

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_text', methods=['POST'])
def process_text():
    text = request.form['input_text']
    # Do something with the text here
    # For example, you can print it to the console
    print("Received text:", text)
    return 'Text received: ' + text

if __name__ == '__main__':
    app.run(debug=True)

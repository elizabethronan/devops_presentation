from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from front page!'

@app.route('items')
def list_items():
    return 'Listing items from amazon db'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
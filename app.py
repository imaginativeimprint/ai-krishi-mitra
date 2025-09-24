import google.generativeai as genai
from flask import Flask, request, jsonify, render_template

# Replace with your actual API Key
API_KEY = "AIzaSyCqYYTJKI8i0UxN9dZ1AvtprezeT3nA7Jw"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

app = Flask(__name__)

# Route to render the main HTML page
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint to handle user messages
@app.route('/chat', methods=['POST'])
def chat_with_jarvis():
    user_input = request.json.get('message')
    if user_input:
        response = chat.send_message(user_input)
        return jsonify({'jarvis_response': response.text})
    return jsonify({'error': 'No message provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)
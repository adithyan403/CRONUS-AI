# Step 5: The Flask Web Server with .env support

from flask import Flask, render_template, request, jsonify
from brainpy import PersonalAI
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Initialize the Flask app
app = Flask(__name__)

# Create a single instance of our AI.
ai = PersonalAI()

# This is the main route. When you go to the website, this function runs.
@app.route('/')
def home():
    # It sends the index.html file to be displayed in the browser.
    return render_template('index.html')

# This route is for handling the messages sent from the webpage.
@app.route('/ask', methods=['POST'])
def ask():
    # Get the user's message from the data sent by the webpage
    user_message = request.json['message']
    
    # Process the message using our AI brain
    ai_response = ai.process_input(user_message)
    
    # Send the AI's response back to the webpage
    return jsonify({'response': ai_response})

# This makes the app run when you execute the script.
if __name__ == '__main__':
    app.run(debug=True)


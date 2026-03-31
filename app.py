from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    message = data.get('message', '').lower() #getting the message from the JSON data
    reposnze_text = ''
    
    if 'hello' in message:
        response_text = 'Hello! How can i assist you today?'
    elif 'help' in message:
        response_text = 'Sure what I can do for you?'
    else:
        response_text = 'I am sorry, I dont think i understand that. CAn you rephrase?'
        
    return jsonify({'reponse': response_text})


if __name__ == '__main__':
    app.run(port=5000, debug=True)
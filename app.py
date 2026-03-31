# Copyright 2026 Lee Marc C. Macalanda
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
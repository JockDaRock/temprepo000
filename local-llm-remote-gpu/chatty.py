from flask import Flask, request, jsonify
from gpt4all import GPT4All

# model = GPT4All('orca-mini-3b-gguf2-q4_0.gguf')
model = GPT4All('yarn-llama-2-13b-64k.Q4_K_M.gguf', model_path="/usr/src/JuiceClient/app", allow_download=False)

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat_with_model():
    # Prompt
    data = request.json
    prompt = data.get('prompt')
    temp = data.get('temp', 0)  # Use default temperature of 0 if not provided
    
    # If prompt
    if prompt is None:
        return jsonify({'error': 'No prompt provided'}), 400

    # Response Time
    # model = GPT4All(model_name='orca-mini-3b-gguf2-q4_0.gguf')
    with model.chat_session():
        response = model.generate(prompt=prompt, temp=temp)
    
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

from flask import Flask, request, jsonify, render_template
import ChatGPT_POC1




app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['GET'])
def chat():
    user_input = request.form.get('user_input')
    response = ChatGPT_POC1.process_user_input(user_input)
    #print(response)
    return render_template('index.html',response=response)

if __name__ == '__main__':
    app.run(debug=True)
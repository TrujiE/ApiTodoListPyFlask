from flask import Flask,jsonify,request
app = Flask(__name__)

# These two lines should always be at the end of your app.py file.
todos=[{"label": "My first task", "done": False}]
@app.route('/todos', methods=['GET'])
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    print("Incoming request with the following body", request_body)
    return 'Response for the POST todo'

def hello_world():
    json_text=jsonify(todos)
    return json_text

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

from flask import Flask, jsonify, request

# Run the API using this in the terminal:
# flask --app {Path to repo}/csc132-itemframe/API/main run

app = Flask(__name__)

postData = []


@app.route("/", methods=['GET'])
def hello_world():
    # Sends the data in the list as a response
    return jsonify(postData)

@app.route("/", methods=['POST'])
def matrix_input():
    postData.append(request.get_json())
    # Just adds data sent to the list. 204 code response
    return "", 204

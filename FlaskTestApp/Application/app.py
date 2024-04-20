import os
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)  # Flask constructor
reverse_sentence = ""


@app.route('/reverse', methods=['GET'])
def reverse():
    global reverse_sentence

    # Get the input string from the "in" query parameter
    input_string = request.args.get('in', '')

    reverse_string = input_string.split(' ')
    reverse_sentence = ' '.join(reversed(reverse_string))

    # Create a JSON response with a field named "out"
    response_data = {"result": reverse_sentence}

    # Return the JSON response
    return jsonify(response_data)


@app.route('/restore')
def restore():
    # restore string
    words = reverse_sentence.split(' ')
    sentence = ' '.join(reversed(words))

    # Create a JSON response with a field named "Source"
    response_data = {"Source": sentence}

    # Return the JSON response
    return jsonify(response_data)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':
    app.run(host='0.0.0.0')

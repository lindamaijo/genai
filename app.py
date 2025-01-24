from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_text():
    
    data = request.json
   
    if not data or 'text' not in data:
        return jsonify({"error": "Invalid input, 'text' field is required"}), 400

    input_text = data['text']


    number = len(input_text)  # Example: Return the length of the text
    response_text = input_text.upper()  # Example: Convert text to uppercase

    # Return the response as JSON
    return jsonify({
        "number": number,
        "text": response_text
    })

if __name__ == '__main__':
    app.run(debug=True)

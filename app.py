from flask import Flask, request, jsonify

app = Flask(__name__)

# POST /bfhl


@app.route('/bfhl', methods=['POST'])
def process_data():
    data = request.json.get('data', [])
    user_id = "pushkar_joshi_02082003"
    email = "pushkar91949@gmail.com"
    roll_number = "21BCG10033"

    numbers = [x for x in data if x.isdigit()]
    alphabets = [x for x in data if x.isalpha()]
    highest_lowercase_alphabet = [max([x for x in data if x.islower()])] if any(
        x.islower() for x in data) else []

    response = {
        "is_success": True,
        "user_id": user_id,
        "email": email,
        "roll_number": roll_number,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": highest_lowercase_alphabet
    }
    return jsonify(response)

# GET /bfhl


@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1})


if __name__ == '__main__':
    app.run(debug=True)

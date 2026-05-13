from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask Server Running Successfully!"

@app.route('/add')
def add():
    try:
        a = int(request.args.get('a'))
        b = int(request.args.get('b'))

        return jsonify({"result": a + b})

    except (TypeError, ValueError):
        return jsonify({
            "error": "Please provide valid integers for 'a' and 'b'."
        })

if __name__ == '__main__':
    app.run(debug=True)
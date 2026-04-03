from flask import Flask, request, jsonify

app = Flask(__name__)

# Method 1: Largest of three (Short version)
@app.route('/largest')
def find_largest():
    # Grabs a, b, and c directly from the URL and finds the max
    vals = [int(request.args.get(x)) for x in ['a', 'b', 'c']]
    return jsonify({"largest": max(vals)})

# Method 2: Multiplication table (Short version)
@app.route('/table/<int:num>')
def get_table(num):
    return jsonify({i: num * i for i in range(1, 11)})

if __name__ == '__main__':
    app.run(debug=True)


#http://127.0.0.1:5000/largest?a=10&b=50&c=25
#http://127.0.0.1:5000/table/5

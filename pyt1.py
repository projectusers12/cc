from flask import Flask, jsonify, request

app=Flask(__name__)

#Home route
@app.route("/")
def home():
    return "Python Web Service is running!"

#Simple GET web service
@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello from Python Web Service"})

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method=="POST":
        data=request.get_json()
        a=data.get("a")
        b=data.get("b")
    else:
        a=int(request.args.get("a"))
        b=int(request.args.get("b"))

        return jsonify({"result": a+b})

if __name__=="__main__":
    app.run(debug=True)

#/hello
#/add/?a=10&b=20
#py -3.12 run.py
#python run.py


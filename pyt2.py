from flask import Flask, jsonify, request

app = Flask(__name__)

# Our "Database"
students = {
    "101": {"name": "Rahul", "marks": 85},
    "102": {"name": "Preshit", "marks": 95}
}

@app.route("/")
def home():
    return "Student Service is Running!"

# 1. View all students: /students
@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)

# 2. View one student: /students/101
@app.route("/students/<id>", methods=["GET"])
def get_student(id):
    if id in students:
        return jsonify(students[id])
    return jsonify({"error": "Student not found"}), 404

# 3. Add student via Browser: /addstudents?id=103&name=Kasturi&marks=12
@app.route("/addstudents", methods=["GET"])
def add_student_browser():
    sid = request.args.get("id")
    name = request.args.get("name")
    marks = request.args.get("marks")

    if not sid or not name or not marks:
        return jsonify({"error": "Missing parameters"}), 400
    
    # Store data (converting marks to int for math/sorting later)
    students[sid] = {"name": name, "marks": int(marks)}
    return jsonify({"message": f"Student {name} added successfully", "current_database": students})

if __name__ == "__main__":
    app.run(debug=True)

#addstudents?id=101&name="kasturi"&marks=12
#/students
#/students/101

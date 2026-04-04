from fastapi import FastAPI
app = FastAPI()

# Sample Employee Data
employees = {
    1: {"name": "Ravi", "department": "HR", "salary": 40000},
    2: {"name": "Priya", "department": "IT", "salary": 55000}
}

# Home Route
@app.get("/")
def home():
    return {"message": "Employee API Running"}

# Get all employees
@app.get("/employees")
def get_employees():
    return employees

# Get employee by ID
@app.get("/employees/{id}")
def get_employee(id: int):
    if id in employees:
        return employees[id]
    return {"error": "Employee not found"}


python -m uvicorn emp_api:app --reload --port 8000
http://localhost:8000/employees



using System;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    static async Task Main()
    {
        using var client = new HttpClient();

        var response = await client.GetAsync("http://localhost:8000/employees");
        var content = await response.Content.ReadAsStringAsync();

        Console.WriteLine("Employee Data from Python API:");
        Console.WriteLine(content);
    }
}

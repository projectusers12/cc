py -3.12 -m pip install fastapi uvicorn


from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello(name: str = "World"):
    return {"message": f"Hello {name} from Python API!"}

py -3.12 -m uvicorn cc:app --reload --port 8000

Console app.net core

using System;
using System.Net.Http;
using System.Threading.Tasks;


namespace prac9
{
    class Program
    {
        static async Task Main()
        {
            using var client = new HttpClient();
            var response = await client.GetAsync("http://localhost:8000/hello?name=Swarnal");
            var content = await response.Content.ReadAsStringAsync();
            Console.WriteLine("Response from Python API:");
            Console.WriteLine(content);
        }
    }
}










py -3.12 -m uvicorn cc:app --reload --port 8000
run program.cs file

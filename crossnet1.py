asp.net core web application

[HttpGet("{name}")]
public string GetHello(string name)
{
    return $"Hello {name} from.NET";
}
run


import requests
url="https://localhost:44342/Swarnal"
response=requests.get(url, verify=False)
print(response.text)

Pip install command py -3.12 -m pip install requests

ASP .NET Core Web Application / App (MVC)
[HttpGet("c2f/{c}")]
public string CelsiusToFahrenheit(double c)
{
    double f = (c * 9 / 5) + 32;
    return $"Celsius {c} = Fahrenheit {f}";
}


[HttpGet("f2c/{f}")]
public string FahrenheitToCelsius(double f)
{
    // Using 5.0 / 9.0 ensures the division is precise
    double c = (f - 32) * 5.0 / 9.0;
    return $"Fahrenheit {f} = Celsius {c}";
}


https://localhost:44380/c2f/25


import requests
url = "https://localhost:44380/c2f/30"
response = requests.get(url, verify=False)
print(response.text)

py -3.12 -m pip install requests
Pip install command py -3.12 -m pip install requests


Select ASP.NET Web Application (.NET Framework)

Asmx
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Services;

namespace WebApplication1
{
    /// <summary>
    /// Summary description for WebService1
    /// </summary>
    [WebService(Namespace = "http://tempuri.org/")]
    [WebServiceBinding(ConformsTo = WsiProfiles.BasicProfile1_1)]
    [System.ComponentModel.ToolboxItem(false)]
    // To allow this Web Service to be called from script, using ASP.NET AJAX, uncomment the following line. 
    // [System.Web.Script.Services.ScriptService]
    public class WebService1 : System.Web.Services.WebService
    {

        [WebMethod]
        public string HelloWorld()
        {
            return "Hello World";
        }

        [WebMethod]
        public double CelsiusToFarheneit(double c)
        {
            return (c * 9 / 5) + 32;
        }

        [WebMethod]
        public double farheneittoCelsius(double f)
        {
            return (f - 32) * 5 / 9;
        }
    }
}



aspx

        protected void Button2_Click(object sender, EventArgs e)
        {
            WebService1 t1 = new WebService1();

            // 2. Get value from TextBox2, send to Service, and display in result2 Label
            Label2.Text = t1.farheneittoCelsius(Double.Parse(TextBox2.Text)).ToString() + " °C";
        }

        

        protected void Button1_Click1(object sender, EventArgs e)
        {
            WebService1 t = new WebService1();

            // 2. Get value from TextBox1, send to Service, and display in result1 Label
            // Double.Parse converts the text "25" into the number 25.0
            Label1.Text = t.CelsiusToFarheneit(Double.Parse(TextBox1.Text)).ToString() + " °F";
        }
  

Aspx normal
<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="WebForm1.aspx.cs" Inherits="WebApplication1.WebForm1" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body style="height: 250px">
  <form id="form1" runat="server">
    <div >
        <h3>Celsius to Fahrenheit</h3>
        <p>
            Value: <asp:TextBox ID="TextBox1" runat="server"></asp:TextBox>
            <asp:Button ID="Button1" runat="server" OnClick="Button1_Click1" Text="Convert" />
        </p>
        <p>
            Result: <asp:Label ID="Label1" runat="server" Text="..."></asp:Label>
        </p>

        <hr />

        <h3>Fahrenheit to Celsius</h3>
        <p>
            Value: <asp:TextBox ID="TextBox2" runat="server"></asp:TextBox>
            <asp:Button ID="Button2" runat="server" OnClick="Button2_Click" Text="Convert" />
        </p>
        <p>
            Result: <asp:Label ID="Label2" runat="server" Text="..."></asp:Label>
        </p>
    </div>
</form>

    </body>
</html>



<dependency>
    <groupId>com.sun.xml.ws</groupId>
    <artifactId>jaxws-rt</artifactId>
    <version>2.3.3</version>
</dependency>


package com.my.prac;
import javax.jws.WebService;
import javax.jws.WebMethod;

@WebService
public class HelloService {
    @WebMethod
    public String sayHello(String name) {
        return "Hello " + name + " ! ";
    }
}


package com.my.prac;
import javax.jws.WebService;
import javax.jws.WebMethod;

@WebService
public class MathService {
    @WebMethod
    public String getSquareAndCube(int num) {
        int sq = num * num;
        int cb = num * num * num;
        return "Square: " + sq + " | Cube: " + cb;
    }
}

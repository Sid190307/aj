import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/HelloServlet")
public class HelloServlet extends HttpServlet {

    @Override
    protected void doGet(
            HttpServletRequest request,
            HttpServletResponse response)
            throws ServletException, IOException {

        response.setContentType("text/html;charset=UTF-8");

        response.getWriter().println("Hello from HelloServlet");
    }
}

mkdir C:\Tomcat9\webapps\HelloApp\WEB-INF\classes

javac -cp "C:\Tomcat9\lib\servlet-api.jar" -d "C:\Tomcat9\webapps\HelloApp\WEB-INF\classes" HelloServlet.java

C:\Tomcat9\bin\startup.bat

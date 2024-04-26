import java.net.*;
import java.io.*;
public class Server {
    public static void main(String[] args) {
        try{
            ServerSocket serverSocket = new ServerSocket(5000);
            System.out.println("Server started!");

            Socket clientSocket = serverSocket.accept();
            System.out.println("Client connected!");

            BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
            PrintWriter out = new  PrintWriter(clientSocket.getOutputStream(), true);
            BufferedReader consoleInput = new BufferedReader(new InputStreamReader(System.in));

            String clientMessage = "";
            String serverMessage = "";

            while(true){
                clientMessage = in.readLine();
                System.out.println("Client: " + clientMessage);

                if(clientMessage.equalsIgnoreCase("bye")){
                    break;
                }

                System.out.print("You: ");
                serverMessage = consoleInput.readLine();
                out.println(serverMessage);
            }

            in.close();
            out.close();
            clientSocket.close();
            serverSocket.close();

        }catch(Exception e){
            System.out.println(e);
        }
    }
}
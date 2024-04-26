import java.io.*;
import java.net.*;

public class Client{
    public static void main(String[] args){
        try{
            Socket socket = new Socket("localhost", 5000);
            
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader consoleInput = new BufferedReader(new InputStreamReader(System.in));

            String clientMessage;
            String serverMessage;

            while(true){
                System.out.print("You: ");
                clientMessage = consoleInput.readLine();
                out.println(clientMessage);

                if(clientMessage.equalsIgnoreCase("bye")){
                    break;
                }

                serverMessage = in.readLine();
                System.out.println("Server: " + serverMessage);

            }

            in.close();
            out.close();
            consoleInput.close();
            socket.close();
        }catch(Exception e){
            System.out.println(e);
        }

    }
}
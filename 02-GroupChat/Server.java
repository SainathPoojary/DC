import java.util.*;
import java.io.*;
import java.net.*;

public class Server{

    private static HashSet<PrintWriter> clientWriters = new HashSet<PrintWriter>();

    public static void main(String[] args){
        try{
            ServerSocket serverSocket = new ServerSocket(5000);
            System.out.println("Server started!");
            while(true){
                new CliendHandler(serverSocket.accept()).start();
            }
        }catch(Exception e){
            System.out.println(e);
        }
    }


    private static class CliendHandler extends Thread{
        Socket clientSocket;
        CliendHandler(Socket socket){
            clientSocket = socket;
        }


        public void run(){
            String name="";
            try{
                BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);

                clientWriters.add(out);

                out.println("What is your name: ");
                name = in.readLine();
                broadcast(name + " has joined the chat!");
                String clientMessage;

                while((clientMessage = in.readLine()) != null){
                    broadcast(name+ ": "+clientMessage);
                }


            } catch(Exception e){
                System.out.println(e);
            } finally{
                broadcast(name + " has left chat!");
            }
        }

        public static void broadcast (String message){
            for (PrintWriter out : clientWriters){
                out.println(message);
            }
        }
    }
}
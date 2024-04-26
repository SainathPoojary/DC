import java.net.*;
import java.io.*;

public class Client{
    public static void main(String[] args){
        try{
            Socket socket = new Socket("localhost",5000);
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader consoleInput = new BufferedReader(new InputStreamReader(System.in));

            new Thread(() -> {
                String serverMessage;
                try{
                    while((serverMessage = in.readLine()) != null){
                        System.out.println(serverMessage);
                    }
                } catch (Exception e){
                   System.out.println(e);
                }
            }).start();


            out.println(consoleInput.readLine());

            while(true){
                String clientMessage = consoleInput.readLine();
                out.println(clientMessage);
                if(clientMessage.equals("bye")){
                    break;
                }
            }

            socket.close();
            in.close();
            out.close();
            consoleInput.close();

        }catch (Exception e){
            System.out.println(e);
        }

    }
}
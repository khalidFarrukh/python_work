using System;
using System.Net;
using System.Net.Sockets;
using System.Text;


public class socket_listener
{
    public static void Start_server()
    {
        IPHostEntry host = Dns.GetHostEntry(Dns.GetHostName());
        int port = 1025;
        IPAddress ip_Address = host.AddressList[0];
        IPEndPoint local_endpoint = new IPEndPoint(ip_Address,port);
        try
        {
            Socket listener = new Socket(ip_Address.AddressFamily, SocketType.Stream, ProtocolType.Tcp);
            listener.Bind(local_endpoint);
            listener.Listen(10);
            Console.WriteLine("Waiting for a connection...");
            Socket handler = listener.Accept();
            String data = null;
            byte[] bytes = null;
            while (true)
            {
                bytes = new byte[1024];
                int bytesRec = handler.Receive(bytes);
                data += Encoding.ASCII.GetString(bytes,0,bytesRec);
                if (data.IndexOf(("<EOF>")) > -1)
                {
                    break;
                }
            }
            Console.WriteLine("Text received :{0}",data);

            byte[] msg = Encoding.ASCII.GetBytes(data);
            handler.Send(msg);
            handler.Shutdown(SocketShutdown.Both);
            handler.Close();
        }
        catch (Exception e)
        {
            Console.WriteLine(e.ToString());
        }
        Console.WriteLine("\n Press any key to continue....");
        Console.ReadKey();

    }
    public static int Main(String[] args)
    {
        Start_server();
        return 0;
    }

}
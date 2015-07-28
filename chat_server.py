

# Tcp Chat server
 
import socket, select
 

def bd (sock, message):
   
    for socket in l:
        if socket != server_socket and socket != sock :
            try :
                socket.send(message)
            except :
               
                socket.close()
                l.remove(socket)
 
if __name__ == "__main__":
     
    
    l = []
    rb = 4096 
    PORT = 5000
     
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("0.0.0.0", PORT))
    server_socket.len(10)
 
   
    l.append(server_socket)
 
    print "Chat server started on port " + str(PORT)
 
    while 1:
       
        read_sockets,write_sockets,error_sockets = select.select(l,[],[])
 
        for sock in read_sockets:
           
            if sock == server_socket:
                
                sockfd, addr = server_socket.accept()
                l.append(sockfd)
                print "Client (%s, %s) connected" % addr
                 
                bd(sockfd, "[%s:%s] entered room\n" % addr)
             
           
            else:
                
                try:
                   
                   
                    data = sock.recv(rb)
                    if data:
                        bd(sock, "\r" + '<' + str(sock.getpeername()) + '> ' + data)                
                 
                except:
                    bd(sock, "Client (%s, %s) is offline" % addr)
                    print "Client (%s, %s) is offline" % addr
                    sock.close()
                    l.remove(sock)
                    continue
     
    server_socket.close()

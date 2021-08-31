import socket
def re(me,ho):
    hostname =ho
    
    HOST = ho # Standard loopback interface address (localhost)
    PORT = 5002       # Port to listen on (non-privileged ports are > 1023)
    print("in reciever folder")
    #print(ho)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(5)
        print("listening")
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(me)
        s.close()

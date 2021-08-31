import socket
import tkinter as tk
def se():

    HOST = '192.168.0.103'  # The server's hostname or IP address
    PORT = 5002        # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b'Face Detected!')
        data = s.recv(1024)

    print('Received', repr(data))
    root=tk.Tk()
    root.title('person')
    tk.Label(root, text=data, font=("Arial Bold",28)).pack()
    root.after(5000,lambda: root.destroy())
    root.mainloop()
    s.close()
    
 

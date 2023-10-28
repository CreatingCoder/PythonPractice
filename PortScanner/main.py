import socket
import sys
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

top = Tk()
top.title('Port Scanner')


L1 = Label(top, text="Host to Scan: ")
L1.grid(row=0, column=0, padx=20, pady=20)
op_array=[]


def display_ports():
   global user_input
   global op_array 
   host =  entry.get()

   for port in range(1, 2150):
        try:
                server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server.bind((host, port))

        except:
                op_array.append(port)
                #print(port)

   msg=messagebox.showinfo( "Scan Completed", 'The Open ports are:' + str(op_array))
   

entry = Entry(top, bd =4)
entry.grid(row=0, column=1, padx=20, pady=20)


B = Button(top, text ="Begin Scan", command = display_ports)
B.grid(row=1, column=1,padx=20, pady=20)


top.mainloop()





















#scan_tgt =input('Please enter the host to scan: ')
# scan_tgt = '127.0.0.1'
# host = socket.gethostbyname(scan_tgt)




# for port in range(1, 2150):
#         try:
#                 server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
#                 server.bind((host, port))

#         except:
#                 #print('open port')
#                 print(port)







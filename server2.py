import socket
import tkinter as tk
import threading

def disp_win(label, count):
    win = tk.Tk()
    win.title("通知受信")
    win_pos = "400x40+40+{}".format(str(count*100+100))
    win.geometry(win_pos)

    label = tk.Label(win, text=label, anchor=tk.W)
    label.pack(fill=tk.X)

    win.mainloop()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 50001))
s.listen(5)

count = 1

while True:
    client, address = s.accept()
#    print(f"Connection from {address} has been established!")
    data = client.recv(1024)
    message = (data.decode("utf-8"))
    print(message)
    th = threading.Thread(target=disp_win, args=(message,count))
    th.start()
    client.close()
    count += 1

import socket
import threading
target='10.2.10.1'  # Target website name
def portscan(port):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        con=s.connect((target,port))
        print('port:',port,"is open.")
        con.close()
    except:
        pass
r=1
for x in range(1,100):
    t=threading.Thread(target=portscan,kwargs={'port':r})
    r+=1
    t.start()
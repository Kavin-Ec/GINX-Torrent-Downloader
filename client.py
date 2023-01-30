import socket
server="127.0.0.1"
port=8080
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((server,port))
print("Enter the Torrent Name:")
tname=input()
client.send(str(tname).encode('utf8'))
name=client.recv(1024)
print("File Name is :",name.decode())
#thash=client.recv(1024)
#print("Hash :",thash.decode())
#seed=client.recv(10240)
#print("Seeds :",seed.decode())
#size=client.recv(1024)
#print("Size :",size.decode())
#ds=client.recv(1024)
#print("Download Speed :",ds.decode())

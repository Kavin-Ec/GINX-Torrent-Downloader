# GINX-Torrent-Downloader
Problem description:
An advanced and multi-platform BitTorrent client with a nice Qt user interface as well as a Web UI for remote control used for downloading torrent files. qBittorrent aims to meet the needs of most users while using as little CPU and memory as possible. Torrent client is a software for downloading files that utilize a peer to peer system. This torrent client allows you to find the files, download them more quickly, and manage them all in one accessible place.

TCP Server – 
1.	Creates a socket by calling the socket() function. The socket() function returns a socket which is not in the state of accepting connections. The socket is also not specifically bound to an address and a port at the server.
2.	The socket() object obtained has to be bound to an address and a port. This is needed because the clients of this server program should know which IP address and port number at which they should connect to.
3.	Step 2 is achieved by calling the bind() method by passing the IP address and port as a pair
4.	Now having the socket created and bound to a specific IP address and Port at the server, the socket needs to be moved to a statewhere it waits for client connections.
5.	By calling the listen() method the socket enters into the TCP state WAIT.
6.	The server receives the either torrent file or magnet link and starts the downloading.
7.	Then web UI gets enabled and the status of the downloading can be seen in webpage local host(127.0.0.1 :1000)
TCP Client – 
1.	The client program creates a socket by calling the socket() function
2.	Calls connect() method, specifying the IP address and the port number of the server program
3.	Then using the UI created with TKINTER the input is fetched,the Torrent file or magnetic link is sended
4.	It initiates sending messages to the server by calling send() with byte sequence
5.	Through recv()calls the client receives any message sent from the server
6.	The connection is explicitly closed by calling the close() on the socket.

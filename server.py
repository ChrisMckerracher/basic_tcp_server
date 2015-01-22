import socket
import sys
import os
import threading 
import time

#generic framework for creating future apps

class server_info:
    #stores basic server info
    def __init__(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = port
        self.host = host
        self.serve_info = (self.host, self.port)

class server:
    #the server class. acts as a container for everything else
    def __init__(self, serve_info):
        self.server_info = serve_info #server_info object
        self.server = self.server_info.socket
        self.server.bind(self.server_info.serve_info)
        self.connection_manager = connection_manager(self.server)

    def init(self):
        self.server.listen(1)
        print('b')
        threading.Thread(target=self.connection_manager.listen).start() 
        #runs in background to build up list of connections
        #should compare with a buffer, add to buffer under any changes
        
    def manage_connection(self):
       #temp implementation
       while True:
           print('a')
           print(self.connection_manager.connections())
        
class connection_handler:
    #handles generic connection stuff per one connection
    def __init__(self, connection):
        self.connection = connection
            
    def read_data(self):
        data = self.connection.recv(16) #redefine size in a more interesting way
        print(("recieved%s" % str(data)[2:-1]))
        return data

    def send_data(self, data):
        self.connection.sendall(data)

    def close(self):
        self.connection.close()

class connection_manager:
    #acts as a container for all connections
    def __init__(self,server):
        self.server = server
        self.connection_dict = {} #this will be a list of connection_handlers
    
    def listen(self):
        while True:
            connection, client_address = self.server.accept()
            self.connection_dict[client_address] = connection

    def connections(self):
        return list(self.connection_dict.keys())

        #interaction has to do with parsing data, and responding. this will be
        #done at an app by app basis

server_infos = server_info('0.0.0.0', 879)
servers = server(server_infos)
servers.init()

while True:
    time.sleep(1)
    print(servers.connection_manager.connections()) 
#atm just prints history of connections

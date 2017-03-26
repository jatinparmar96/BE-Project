import os
import glob
import time
import thread
from bluetooth import *


class bluetoothops:
    client_sock = None
    server_sock = None
    client_info = None
    z = 0

    def listenfordata(self, client_socket):
        x = True
        while x:
            try:
                data = client_socket.recv(2048)
                if (len(data) == 0):
                    continue
                else:
                    print "Reacieved %s" % data
                    print type(data)

            except KeyboardInterrupt:
                client_socket.close()
                x = False

    def connect(self):
        global server_sock, client_sock, z, client_info
        server_sock = BluetoothSocket(RFCOMM)
        server_sock.bind(("", PORT_ANY))
        server_sock.listen(1)
        port = server_sock.getsockname()
        uuid = "fa87c0d0-afac-11de-8a39-0800200c9a66"

        advertise_service(server_sock, "RasPiServer",
                          service_id=uuid,
                          service_classes=[uuid, SERIAL_PORT_CLASS],
                          profiles=[SERIAL_PORT_PROFILE],
                          # protocols = [ OBEX_UUID ]
                          )
        print "Waiting for connection on RFCOMM channel %d" % port[1]

        client_sock, client_info = server_sock.accept()
        print type(client_info)
        print "Accepted connection from ", client_info

        thread.start_new_thread(self.listenfordata, (client_sock,))

    def send_data(self, message):
        global client_sock
        try:
            if len(message) >= 1 and message != "":
                client_sock.send(str.encode(message + "#"))
        except:
            print "Client Not Connected"
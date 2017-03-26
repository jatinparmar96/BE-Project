__author__ = 'Jatin'
import Bluetoothreceive
class Send:
    def send_data(self,clientsoc,clientinfo, message):
            try:
               # clientsoc.connect((clientinfo,2))
                clientsoc.send(message+"#")
            except:
                print "Client sock is disconnected"
                raise
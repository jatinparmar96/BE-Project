__author__ = 'Jatin'
import time
import thread

import scanner
from bluetoothoperations import Bluetoothreceive

# imports end

y = True
scanobj = scanner.Scanner();
blueobj = Bluetoothreceive.bluetoothops();
thread.start_new_thread(blueobj.connect, ())
print("Starting execution")
while y:

    fo = open("writetest.txt", "r+")
    data = scanobj.scan();

    string = str.split(fo.read(), '!');
    print(len(string))
    for value in string:
        print(value + "\n")
    for data in string:
        blueobj.send_data(data)
        # sendobj = Sender.Sender();
        # sendobj.data_to_send(data);
        # sendobj.send_data();
        fo.close()
    print("for exited")
    time.sleep(2);

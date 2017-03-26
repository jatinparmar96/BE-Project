__author__ = 'Jatin'


import time
from SimpleCV import *
import zbar
from PIL import Image

class Scanner:
    def __init__(self):
        print ("Starting")

    def scan(self):

        # Open a file
        fo = open("writetest.txt", "wb")
        x=True
        #print "err"
        cam = Camera();
        try:

                  # If you don't wait, the image will be dark
                while x:
                    #print "Image loop"
                    img = cam.getImage()
                    img.save('decodeimage.jpg')
                    time.sleep(0.5)
                    # create a reader
                    scanner = zbar.ImageScanner()

                    # configure the reader
                    scanner.parse_config('enable')

                    # obtain image data
                    pil = Image.open("decodeimage.jpg").convert('L')
                    width, height = pil.size
                    raw = pil.tostring()

                    # wrap image data
                    image = zbar.Image(width, height, 'Y800', raw)
                    # scan the image for barcodes
                    if(scanner.scan(image)):
                        # extract results
                        print "result"
                        for symbol in image:
                            # do something useful with results
                            send_code=symbol.data
                            #print 'decoded', symbol.type, 'symbol', '"%s"' % send_code
                            fo.write(symbol.data + "!");
                            #yield send_code
                        fo.close()
                        x= False

                    #cam.release()
                    # clean up
                    del(image)
                    #x=False;
        except:
                del(cam)
                raise
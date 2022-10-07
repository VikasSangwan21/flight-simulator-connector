from pySerialTransfer import pySerialTransfer as txfer
from time import sleep
from simData import *

ArduinoCommunicationPort = 'COM5'

if __name__ == '__main__':
    try:
        
        #Open connection to arduino com port
        link = txfer.SerialTransfer(ArduinoCommunicationPort)    
        link.open()
        sleep(2) # allow some time for the Arduino to completely reset
        currentValues = []
        print("****By VBUILDS**** Sending Data to Simulator Panels ")
        while True:
            send_size = 0
            
            ###################################################################
            # Send a List
            ###################################################################
            
            currentValues = getSimVarString()
            if(len(currentValues)>1):   
                str_size = link.tx_obj(currentValues, send_size) - send_size
                send_size += str_size

                ###################################################################
                # Transmit all the data to send in a single packet
                ###################################################################
                link.send(send_size)
                
                
                print('SENT: {}'.format(currentValues))
                #sleep(2)
                link.
                
    except KeyboardInterrupt:
        try:
            link.close()
        except:
            pass
    
    except:
        import traceback
        traceback.print_exc()
        
        try:
            link.close()
        except:
            pass
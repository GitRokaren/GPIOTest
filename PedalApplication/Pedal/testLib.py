import gpiozero
from gpiozero.output_devices import LED
from gpiozero.input_devices import Button

class testLib(object):

    ROBOT_LIBRARY_VERSION = 1.0

    def __init__(self):
        
        pass

    def Hello(self):
        print("Hello There")
        
    def FUCK(self):
        print("FUCK")

    def confOutPin(self, Nr, Value):
            if(Value == 1):
                LED(Nr).on()
            else:
                LED(Nr).off()
                
    def readInPin(self, Nr):
        return Button(Nr).is_active()

                
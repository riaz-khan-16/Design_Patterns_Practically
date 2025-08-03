class Device:
       def turnOn(self):
              pass
       def turnOff(self):
              pass
       
class TV:
       def turnOn(self):
              print("TV is On")
       def turnOff(self):
              print("TV is OFF")
class Radio:
       def turnOn(self):
              print("Radio is On")
       def turnOff(self):
              print("Radio is OFF")

class Fan:
       def turnOn(self):
              print("Fan is On")
       def turnOff(self):
              print("Fan is OFF")

class Remote:
       def __init__(self, device:Device):
            self.device=device
       def press_on(self):
            self.device.turnOn()
       def press_off(self):
            self.device.turnOff()
tv=TV()
fan=Fan()
radio=Radio()


remote=Remote(tv)
remote.press_on()
remote=Remote(radio)
remote.press_on()
remote=Remote(fan)
remote.press_on()
remote.press_off()
from abc import ABC,abstractmethod
class Smart_devices(ABC):
    def command_status(self):
        pass
class SmartFan(Smart_devices):
    def command_status(self):
        print('Smart Fan is active!')
    def someone_at_door(self):
        pass
class SmartTV(Smart_devices):
    def command_status(self):
        print('Smart TV is active!')
    def someone_at_door(self):
        pass
class SmartDoorBell(Smart_devices):
    def command_status(self):
        print('Smart Doorbell is active!')
    def someone_at_door(self):
        print('Alert! (Someome is ringing the doorbell!) ')
class SmartCamera(Smart_devices):
    def command_status(self):
        print('Smart Camera is active!')
    def someone_at_door(self):
            print('Alert! (The person is identified as Advik!) ')
class SmartThermostat(Smart_devices):
    def command_status(self):
        print('Smart Thermostat is disabled!')
    def someone_at_door(self):
        pass
sf = SmartFan()
stv = SmartTV()
sdb = SmartDoorBell()
sc = SmartCamera()
st = SmartThermostat()
commands = [sf,stv,sdb,sc,st]
for i in commands:
    i.command_status()
    i.someone_at_door()

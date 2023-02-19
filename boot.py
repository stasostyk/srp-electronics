import board
import storage

# Remame drive to 'SRP-DARE-FC' 
storage.remount('/', readonly=False)

m = storage.getmount('/')
m.label = 'SRP-DARE-FC'

storage.remount('/', readonly=True)

storage.enable_usb_drive()

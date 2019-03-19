import pygatt

# The BGAPI backend will attemt to auto-discover the serial device name of the
# attached BGAPI-compatible USB adapter.
adapter = pygatt.BGAPIBackend(serial_port='COM3')


adapter.start()
device = adapter.connect('C0:EC:09:EA:D4:5D')
# value = device.char_read("a1e8f5b1-696b-4e4c-87c6-69dfe0b0093b")
rssi = device.get_rssi()
print(rssi)

adapter.stop()

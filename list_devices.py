from evdev import InputDevice, list_devices

for device in list_devices():
    input = InputDevice(device)
    print(input)
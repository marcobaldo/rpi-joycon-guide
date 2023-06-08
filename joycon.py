import asyncio
from evdev import InputDevice, ecodes

joycon = InputDevice('/dev/input/event6')

button_states = {0: 'Released', 1: 'Pressed'}
button_mapping = {
    544: 'UP',
    545: 'DOWN',
    546: 'LEFT',
    547: 'RIGHT',

    304: 'B',
    305: 'A',
    307: 'X',
    308: 'Y',

    309: 'CAPTURE',

    310: 'L',
    311: 'R',
    312: 'ZL',
    313: 'ZR',

    314: 'MINUS',
    315: 'PLUS',
    316: 'HOME',

    317: 'L_STICK',
    318: 'R_STICK'
}

stick_mapping = {
    0: ('LSTICK', 'Y'),
    1: ('LSTICK', 'X'),
    3: ('RSTICK', 'Y'),
    4: ('RSTICK', 'X')
}

def get_button(code):
    return button_mapping.get(code, 'UNKNOWN')

def get_button_state(value):
    return button_states.get(value, 'UNKNOWN')

def get_stick(code):
    return stick_mapping.get(code, 'UNKNOWN')

def get_stick_direction(code, value):
    _, ax = get_stick(code)
    if value == 0: return 'CENTER'
    if ax == 'X':
        return 'LEFT' if value < 0 else 'RIGHT'
    
    return 'UP' if value > 0 else 'DOWN'

def handle_button_event(evt):
    print(get_button_state(evt.value), get_button(evt.code))

def handle_stick_event(evt):
    print(get_stick(evt.code), get_stick_direction(evt.code, evt.value), evt.value)


async def print_events(device):
    async for evt in device.async_read_loop():
        if evt.type == ecodes.EV_KEY:
            handle_button_event(evt)
            continue

        if evt.type == ecodes.EV_ABS:
            handle_stick_event(evt)
            continue

asyncio.ensure_future(print_events(joycon))

loop = asyncio.get_event_loop()
loop.run_forever()
import pywinusb.hid as hid

filter = hid.HidDeviceFilter(vendor_id = 4489, product_id = 34882)
hid_device = filter.get_devices()
device = hid_device[0]
device.open()
report = device.find_output_reports()[0]

mappinglayers = {
    "first":{
        "Key1" : "Q",   "Key5" : "Q",   "Key9" :  "Q",
        "Key2" : "Q",   "Key6" : "Q",   "Key10" : "Q",
        "Key3" : "Q",   "Key7" : "B",   "Key11" : "Q",
        "Key4" : "8",   "Key8" : "5",   "Key12" : "1",

        "Knob1Push" :  "SpaceKey",
        "Knob1Left" :  "Ctrl-A",
        "Knob1Right" : "Ctrl-D",

        "Knob2Push" :  "1000s,Q",
        "Knob2Left" :  "U",
        "Knob2Right" : "1000s,Y",

        "Knob3Push" :  "M",
        "Knob3Left" :  "W",
        "Knob3Right" : "E",

        "ledconfig":["red",'blink'],
    },

    "second":{
        "Key1" : "Q",   "Key5" : "Q",   "Key9" :  "Q",
        "Key2" : "Q",   "Key6" : "Q",   "Key10" : "Q",
        "Key3" : "Q",   "Key7" : "Q",   "Key11" : "Q",
        "Key4" : "Q",   "Key8" : "Q",   "Key12" : "Q",

        "Knob1Push" :  "VolMute",
        "Knob1Left" :  "VolDn",
        "Knob1Right" : "VolUp",

        "Knob2Push" :  "PlayPause",
        "Knob2Left" :  "PrevTrack",
        "Knob2Right" : "NextTrack",

        "Knob3Push" :  "PlayPause",
        "Knob3Left" :  "Rewind",
        "Knob3Right" : "FastForward",

        "ledconfig":["dark_green",'solid'],
    },


    "third":{
        "Key1" : "3",   "Key5" : "2",   "Key9" :  "1",
        "Key2" : "6",   "Key6" : "5",   "Key10" : "4",
        "Key3" : "9",   "Key7" : "8",   "Key11" : "7",
        "Key4" : "0",   "Key8" : "0",   "Key12" : "0",

        "Knob1Push" :  "VolMute",
        "Knob1Left" :  "VolDn",
        "Knob1Right" : "VolUp",

        "Knob2Push" :  "MouseLeftKey",
        "Knob2Left" :  "MouseUp",
        "Knob2Right" : "MouseDown",

        "Knob3Push" :  "MouseRightKey",
        "Knob3Left" :  "MouseLeft",
        "Knob3Right" : "MouseRight",
        "ledconfig":["white",'solid'],
    },
}


layers = {
    "first":1,
    "second":2,
    "third":3
}

colors = {
    "random": 0,
    "red": 1,
    "yellow": 2,
    "bight_green": 3,
    "dark_green": 4,
    "cyan": 5,
    "blue": 6,
    "violet": 7,
    "white": 8,
}

modes = {
    "off": 0,
    "solid": 1,
    "blink": 2,
    "breathing": 3,
    "rainbow": 4,
    "snake": 5,
}


keytypes = {
    "None" : 0,
    "Basic" : 1,
    "Multimedia" : 2,
    "Mouse" : 3,
    "LED" : 8,
}

actions = {
    "None" : 0,
    "Key1" : 1,
    "Key2" : 2,
    "Key3" : 3,
    "Key4" : 4,
    "Key5" : 5,
    "Key6" : 6,
    "Key7" : 7,
    "Key8" : 8,
    "Key9" : 9,
    "Key10" : 10,
    "Key11" : 11,
    "Key12" : 12,

    "Knob1Push" :  23,
    "Knob1Left" :  22,
    "Knob1Right" : 24,

    "Knob2Left" :  19,
    "Knob2Push" :  20,
    "Knob2Right" : 21,

    "Knob3Left" :  16,
    "Knob3Push" :  17,
    "Knob3Right" : 18,

    "ledconfig" :  176,
}


modifiers = {
    "Ctrl": 1,
    "Shift": 1 << 1,
    "Alt": 1 << 2,
    "Win": 1 << 3,
    "RightCtrl": 1 << 4,
    "RightShift": 1 << 5,
    "RightAlt": 1 << 6,
    "RightWin": 1 << 7,
    "None": 0,
}

keyMapping = {
    "Basic" : {
        "A" : 4,
        "B" : 5,
        "C" : 6,
        "D" : 7,
        "E" : 8,
        "F" : 9,
        "G" : 10,
        "H" : 11,
        "I" : 12,
        "J" : 13,
        "K" : 14,
        "L" : 15,
        "M" : 16,
        "N" : 17,
        "O" : 18,
        "P" : 19,
        "Q" : 20,
        "R" : 21,
        "S" : 22,
        "T" : 23,
        "U" : 24,
        "V" : 25,
        "W" : 26,
        "X" : 27,
        "Y" : 28,
        "Z" : 29,

        "1" : 30,
        "2" : 31,
        "3" : 32,
        "4" : 33,
        "5" : 34,
        "6" : 35,
        "7" : 36,
        "8" : 37,
        "9" : 38,
        "0" : 39,

        "Enter" : 40,
        "Esc" : 41,
        "Backspace" : 42,
        "Tab" : 43,
        "SpaceKey" : 44,
        "Minus" : 45,
        "Plus" : 46,
        "OpenBracket" : 47,
        "CloseBracket" : 48,
        "Pipe" : 49,
        "Colon" : 51,
        "Backslash" : 52,
        "Tilde" : 53,
        "Clear" : 54,
        "Period" : 55,
        "Question" : 56,
        "CapsLock" : 57,
        "F1" : 58,
        "F2" : 59,
        "F3" : 60,
        "F4" : 61,
        "F5" : 62,
        "F6" : 63,
        "F7" : 64,
        "F8" : 65,
        "F9" : 66,
        "F10" : 67,
        "F11" : 68,
        "F12" : 69,
        "PrtSc" : 70,
        "ScrollLock" : 71,
        "PauseBreak" : 72,
        "Insert" : 73,
        "Home" : 74,
        "PgUp" : 75,
        "Del" : 76,
        "End" : 77,
        "PgDn" : 78,
        "ArrowRight" : 79,
        "ArrowLeft" : 80,
        "ArrowDown" : 81,
        "ArrowUp" : 82,
        "Num" : 83,
        "NumDiv" : 84,
        "NumMul" : 85,
        "NumSub" : 86,
        "NumAdd" : 87,
        "Num1" : 89,
        "Num2" : 90,
        "Num3" : 91,
        "Num4" : 92,
        "Num5" : 93,
        "Num6" : 94,
        "Num7" : 95,
        "Num8" : 96,
        "Num9" : 97,
        "Num0" : 98,
        "NumDec" : 99,
        "NumEnter" : 100,
        "App" : 101,
        "IsoPlus1" : 102,
        "None" : 0,

        "Comma": 54,
        "ForwardSlash": 56,
        "Semicolon": 51,
        "Apostrophe": 52,
        "GraveAccent": 53,

        "F13": 104,
        "F14": 105,
        "F15": 106,
        "F16": 107,
        "F17": 108,
        "F18": 109,
        "F19": 110,
        "F20": 111,
        "F21": 112,
        "F22": 113,
        "F23": 114,
        "F24": 115,

        "Power": 116,
        "Sleep": 117,
        "Wake": 118,
        "Menu": 119,
        "Execute": 120,
        "Help": 121,
        "Select": 122,
        "Stop": 123,
        "Again": 124,
        "Undo": 125,
        "Cut": 126,
        "Copy": 127,
        "Paste": 128,
        "Find": 129,

        "International1": 135,
        "International2": 136,
        "International3": 137,
        "International4": 138,
        "International5": 139,
        "LANG1": 144,
        "LANG2": 145,

        "NUHS": 50,
        "NUBS": 100,
        "ISOBackslash": 102,
        "JISYen": 137,
        "JISRo": 138,

        "NumEquals": 103,
        "NumComma": 104,

    },

    "Mouse" : {
        "MouseLeftKey": [0, 1, 0, 0, 0],
        "MouseMiddleKey": [0, 4, 0, 0, 0],
        "MouseRightKey": [0, 2, 0, 0, 0],
        "MouseWheelUp": [0, 0, 0, 0, 1],
        "MouseWheelDn": [0, 0, 0, 0, 255],
        "CtrlMouseUp": [1, 0, 0, 0, 1],
        "CtrlMouseDn": [1, 0, 0, 0, 255],
        "ShiftMouseUp": [2, 0, 0, 0, 1],
        "ShiftMouseDn": [2, 0, 0, 0, 255],
        "AltMouseUp": [4, 0, 0, 0, 1],
        "AltMouseDn": [4, 0, 0, 0, 255],

        "MouseForward": [0, 8, 0, 0, 0],
        "MouseBack": [0, 16, 0, 0, 0],
        "MouseWheelLeft": [0, 0, 0, 1, 0],
        "MouseWheelRight": [0, 0, 0, 255, 0],
        "CtrlMouseLeft": [1, 1, 0, 0, 0],
        "CtrlMouseRight": [1, 2, 0, 0, 0],
        "AltMouseLeft": [4, 1, 0, 0, 0],
        "AltMouseRight": [4, 2, 0, 0, 0],

        "MouseUp": [0, 0, 0, 256-10, 0],
        "MouseDown": [0, 0, 0, 10, 0],
        "MouseLeft": [0, 0, 256-10, 0, 0],
        "MouseRight": [0, 0, 10, 0, 0],

        "MouseUpLeft": [0, 0, 256-10, 256-10, 0],
        "MouseUpRight": [0, 0, 10, 256-10, 0],
        "MouseDownLeft": [0, 0, 256-10, 10, 0],
        "MouseDownRight": [0, 0, 10, 10, 0],

        "MouseFastUp": [0, 0, 0, 256-50, 0],
        "MouseFastDown": [0, 0, 0, 50, 0],
        "MouseFastLeft": [0, 0, 256-50, 0, 0],
        "MouseFastRight": [0, 0, 50, 0, 0],
    },

    "Multimedia" : {
        "PlayPause": [205, 0, 0],
        "NextTrack": [181, 0, 0],
        "PrevTrack": [182, 0, 0],
        "VolMute": [226, 0, 0],
        "VolUp": [233, 0, 0],
        "VolDn": [234, 0, 0],
        "Stop":[183, 0, 0],
        "Computer":[148, 1, 0],
        "ScreenBritnessUp":[111, 0, 0],
        "ScreenBritnessDn":[111, 0, 0],
        "Multimedial":[131, 1, 0],
        "Calc":[146, 1, 0],
        "Home":[35, 2, 0],
        "Email":[138, 1, 0],
        "BassUp":[82, 1, 0],
        "TrebleUp":[84, 1, 0],
        "TrebleDn":[85, 1, 0],
        "PgRefresh":[39, 2, 0],
        "PgForward":[37, 2, 0],
        "PgBack":[36, 2, 0],

        "Rewind": [180, 0, 0],
        "FastForward": [179, 0, 0],

        "MyComputer": [149, 1, 0],
        "Mail": [138, 1, 0],
        "Calculator": [146, 1, 0],
        "Explorer": [150, 1, 0],
        "Sleep": [151, 1, 0],

        "Favorites": [38, 2, 0],
        "Search": [40, 2, 0],
        "Stop": [41, 2, 0],
        
        "BassDn": [83, 1, 0],
        "Balance": [86, 1, 0],
        "MicMute": [227, 0, 0],
    }
}

filter = hid.HidDeviceFilter(vendor_id = 4489, product_id = 34882)
hid_device = filter.get_devices()
device = hid_device[0]
device.open()
report = device.find_output_reports()[0]

for layername,keys in mappinglayers.items():
    for keyname, keysympaths in keys.items():

        if keyname == 'ledconfig':
            action = actions[keyname]
            layer  = layers[layername]
            color = colors[keysympaths[0]]
            mode = modes[keysympaths[1]]
            delay = 0
            keytype = keytypes['LED']
            keys = [0, (color << 4) | (mode & 0x0F)]

        else:
            action = actions[keyname]
            layer  = layers[layername]
            color = colors['red']
            mode = modes['breathing']
            delay = 0
            keytype = None
            keys = []

            for keysympath in keysympaths.split(','):

                modifer = 0

                keysymparts = keysympath.split('-')
                keysym = ''

                for part in keysymparts:
                    mod   = modifiers.get(part)
                    delay += int(part.replace('s','')) if part.endswith('s') and part.replace('s','').isdigit() else 0
                    if mod is not None:
                        modifer += mod
                    else:
                        keysym+=part

                for keytypename,hidCodeMap in keyMapping.items():
                    tempkeys = hidCodeMap.get(keysym)
                    if tempkeys is not None:

                        if keytypename == "Basic":
                            keys.extend([modifer,tempkeys])
                        else:
                            keys.extend(tempkeys)
                        keytype = keytypes.get(keytypename)
                        break

        if keys is not None and keytype is not None:

            data = bytearray(report.get_raw_data())

            data[1] = 0xfe
            data[2] = action
            data[3] = layer
            data[4] = keytype
            data[5] = delay & 0xFF
            data[6] = (delay >> 8) & 0xFF
            data[10] = len(keys)
            for i,k in enumerate(keys):
                data[11+i] = k

            report.set_raw_data(data)
            result = report.send()

            print(f"{keytypename=},{layername=},{keyname=},{keysympath=},{keysym=},{keys=},{keytype=}",'Loaded' if result else 'Failed')
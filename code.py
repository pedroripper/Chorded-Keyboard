import board
import digitalio
import gc
import time
import touchio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode


# Right hand

touchpad_0 = board.A0
touch_0 = touchio.TouchIn(touchpad_0)
k0 = False

touchpad_1 = board.A1
touch_1 = touchio.TouchIn(touchpad_1)
k1 = False


touchpad_2 = board.A2
touch_2 = touchio.TouchIn(touchpad_2)
k2 = False

touchpad_3 = board.A3
touch_3 = touchio.TouchIn(touchpad_3)
k3 = False


# Left hand

touchpad_4 = board.A4
touch_4 = touchio.TouchIn(touchpad_4)
k4 = False

touchpad_5 = board.A5
touch_5 = touchio.TouchIn(touchpad_5)
k5 = False


touchpad_6 = board.D9
touch_6 = touchio.TouchIn(touchpad_6)
k6 = False



# For QT Py M0:
led = digitalio.DigitalInOut(board.SCK)
led.direction = digitalio.Direction.OUTPUT



key_pin_array = [k0,k1,k2,k3,k4,k5,k6]


# The Keycode sent for each button, will be paired with a control key
keys_letters = [Keycode.A, Keycode.B, Keycode.C, Keycode.D, Keycode.E, Keycode.F, Keycode.G, Keycode.H, Keycode.I, Keycode.J, Keycode.K, Keycode.L, Keycode.M, Keycode.N, Keycode.O, Keycode.P, Keycode.Q, Keycode.R, Keycode.S, Keycode.T, Keycode.U, Keycode.V, Keycode.W, Keycode.X, Keycode.Y, Keycode.Z]
keys_numbers = [Keycode.ONE,Keycode.TWO,Keycode.THREE,Keycode.FOUR,Keycode.FIVE,Keycode.SIX,Keycode.SEVEN,Keycode.EIGHT,Keycode.NINE,Keycode.ZERO]
keys_special = [Keycode.SPACE,Keycode.BACKSPACE,Keycode.ENTER,Keycode.PERIOD]
caps_key = Keycode.CAPS_LOCK


# The keyboard object!
time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)



def getKeysIndex():
    return int(str(k4)+str(k3)+str(k2)+str(k1)+str(k0),2)


def print_touched():
    print("Key 0: ", k0," Key 1: ", k1, " Key 2: ", k2, " Key 3: ", k3)
    print("Key 4: ", k4," Key 5: ", k5, " Key 6: ", k6)


def checkKey():
    i = -1
    #for key_pin in key_pin_array:
        #if key_pin:
    i += getKeysIndex()
    print("Caraca muleque ", i)
    if i >= 0:
        try:
            key = keys_letters[i]  # Get the corresponding Keycode or string
            if k5:
                key = keys_special[i]
            if k6:
                key = keys_numbers[i]


            #keyboard.press(control_key, key)  # "Press"...
            keyboard.press(key)
            keyboard.release_all()  # ..."Release"!
        except:
            pass

        led.value = False

    elif k6:
        keyboard.press(caps_key)
        #keyboard.release_all()  # ..."Release"!
        print("cap")
# ABCDEFGHI
while True:
    if touch_0.raw_value > 3000:
        time.sleep(0.05)
        if touch_0.raw_value > 3000:
            #print("Touched 0")
            k0 = 1
        else:
            k0 = 0
    else:
        k0 = 0
    #print(touch.raw_value)


    #print(touch_1.raw_value)
    if touch_1.raw_value > 2500:
        time.sleep(0.05)
        if touch_1.raw_value > 2500:
            #print("Touched 1")
            k1 = 1
        else:
            k1 = 0
    else:
        k1 = 0



    if touch_2.raw_value > 2500:
        time.sleep(0.05)
        if touch_2.raw_value > 2500:
            #print("Touched 2")
            k2 = 1
        else:
            k2 = 0
    else:
        k2 = 0


    if touch_3.raw_value > 2500:
        time.sleep(0.05)
        if touch_3.raw_value > 2500:
            #print("Touched 2")
            k3 = 1
        else:
            k3 = 0
    else:
        k3 = 0

    if touch_4.raw_value > 2000:
        time.sleep(0.05)
        if touch_4.raw_value > 2000:
            #print("Touched 2")
            k4 = 1
        else:
            k4 = 0
    else:
        k4 = 0


    if touch_5.raw_value > 2000:
        time.sleep(0.05)
        if touch_5.raw_value > 2000:
            #print("Touched 2")
            k5 = 1
        else:
            k5 = 0
    else:
        k5 = 0


    if touch_6.raw_value > 2000:
        time.sleep(0.05)
        if touch_6.raw_value > 2000:
            #print("Touched 2")
            k6 = 1
        else:
            k6 = 0
    else:
        k6 = 0

    print_touched()
    checkKey()
    key_pin_array = [k0,k1,k2,k3,k4,k5,k6]

    print("")
    time.sleep(1)


#

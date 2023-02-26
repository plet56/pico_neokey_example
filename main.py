import machine, neopixel
import random,  time

Button = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_DOWN)
Button2 = machine.Pin(1, machine.Pin.IN, machine.Pin.PULL_DOWN)

NeoP = neopixel.NeoPixel(machine.Pin(3), 3)



mx = 3
while True:
    NeoP[0] = (random.randint(0, mx), random.randint(0, mx), random.randint(0, mx))
    NeoP[1] = (random.randint(0, mx), random.randint(0, mx), random.randint(0, mx))
    NeoP[2] = (random.randint(0, mx), random.randint(0, mx), random.randint(0, mx))
    NeoP.write()
    
    #Note, this is a terrible way of getting button input as it relys on the state of the
    # loop at the time of the button press. It is only useful as a way to prove the buttons
    # are connected properly
    if Button.value():
        print("Button 1 working!")
    elif Button2.value():
        print("Button 2 working!")
    time.sleep(0.4)
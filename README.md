# pico_neokey_example
Example of using neokeys with micropython

Buttons and neopixels are separate entities:

- Buttons: Just a simple circuit (2 wires). Each button needs it's own GPIO connection.

 Connect A to 3v3(out) and C to assigned GPIO. Either side of circuitboard is OK


- Neopixels:

  Power: + to 3v3(out) and - to GND (seemingly controlling white but not actually needed to get something out - there will be light with + only!)

  GPIO: neopixels work in serial and only 1 GPIO pin is required. Connect GPIO to I of first neopixel and O to I of next neopixel. repeat O to I for all neopixels. No O connection required for last neopixel.
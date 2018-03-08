# LED
# The board is a square grid of LEDs which we control by sending commands to the unit to turn on or off certain rectangular regions.
# The L × L lights can be modelled as a 2 dimensional grid with L rows of lights and L lights in each row and the LED's at each corner are (0, 0), (0, L−1), (L−1, L−1) and (L − 1, 0).
# The lights are either on or off.
# Your job is to test the lights. We test them by sending instructions to turn on, turn off, or switch various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.
For example:
# • "turn on 0,0 through 999,999" would turn on (or leave on) every light.
# • "switch 0,0 through 999,0" would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
# • "turn off 499,499 through 500,500" would turn off (or leave off) the middle four lights.

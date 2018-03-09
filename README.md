# LED
# The board is a square grid of LEDs which we control by sending commands to the unit to turn on or off certain rectangular regions.
# The L × L lights can be modelled as a 2 dimensional grid with L rows of lights and L lights in each row and the LED's at each corner are (0, 0), (0, L−1), (L−1, L−1) and (L − 1, 0).
# The lights are either on or off.
# Your job is to test the lights. We test them by sending instructions to turn on, turn off, or switch various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.
For example:
# • "turn on 0,0 through 999,999" would turn on (or leave on) every light.
# • "switch 0,0 through 999,0" would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
# • "turn off 499,499 through 500,500" would turn off (or leave off) the middle four lights.
# 

# 1. Setup
# Enter LED root folder, execute the following command:
#	$sudo python setup.py develop
# Then, you will be able to install console command into local system
# 
# 2. Execution:
# 	$solve_led --input http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_a.txt
#  	or
#	$solve_led --input localpath~/input_assign3_a.txt
# If you need more instructions on this command, run with:
#	#solve_led --help
# If you need more debug information displayed during the execution, run with:
#	$solve_led --input http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_a.txt -d
#
# 3. Limitations:
# Due to the limitation of alghorithm in this solution, this script has not efficient performance when the LED operating instructions are very large. For example, when calculating with input_asign3_a.txt (http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_a.txt), it will take quite a long time to be finished (more than 30 mins). And it is also affected by the memory size of the machine if the light grid size is over 10000 * 10000 matrix.
#
# 4. Testing:
# There are 9 test cases under test/folder. To run them:
#	$py.test LED/tests/test_led.py

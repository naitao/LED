import re
from urllib import request
import argparse
import sys

class LightTester:
    lights = None

    def __init__(self, N):
        self.size = N
        self.lights = [[0] * N for row in range(N)]

    def apply(self, cmd):
        action = cmd[1]
        start_x = int(cmd[2])
        start_y = int(cmd[3])
        end_x = int(cmd[4])
        end_y = int(cmd[5])

        # If the range of all values are outside of the grid, we need to cancel this instruction!
        # So, the following checking does make sense in 2 conditions, althouth they didn't appear
        # on input_assign3_c.txt
        if (start_x < 0 and start_y < 0 and end_x < 0 and end_y < 0) or \
            (start_x >= self.size and start_y >= self.size and end_x >= self.size and end_y >= self.size):
            return

        # If one point is out side of the grid, we need to revise the point to the boundary of the grid
        # Check the values to make sure that they are all in the certain range of grid
        start_x = self.checkValue(start_x)
        start_y = self.checkValue(start_y)
        end_x = self.checkValue(end_x)
        end_y = self.checkValue(end_y)


        # Handle on lights
        if action in 'turn on':
            for i in range(start_x, end_x+1):
                for j in range(start_y, end_y+1):
                    self.lights[i][j] = 1
                    
        elif action in 'turn off':
            for i in range(start_x, end_x+1):
                for j in range(start_y, end_y+1):
                    self.lights[i][j] = 0

        elif action in 'switch': 
            for i in range(start_x, end_x + 1):
                for j in range(start_y, end_y + 1):
                    self.lights[i][j] = (0 if self.lights[i][j] == 1 else 1)

    def checkValue(self, value):
        if value < 0:
            return 0
        elif value >= self.size:
            return (self.size-1)
        else:
            return value

    def count(self):
        count = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.lights[j][i] == 1:
                    count += 1
        return count

def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='solve_led --input "http://~/.txt"')
    parser.add_argument('-d', action="store_true", default=False, help='switch on debug mode')
    # ...Create your parser as you like...
    return parser.parse_args(args)

def get_response(filename):
    '''Get data stream from url address or
       get data stream from a local file'''

    if filename is None:
        return None

    try:
        if 'http' in filename:
            stream = request.urlopen(filename)
        else:
            stream = open(filename, "r")
    except Exception as e:
        print(str(e))
        return None

    return stream

def main():
    args = parse_args(sys.argv[1:])
    isDebug = args.d
    response = get_response(args.input)  
    if response is None:
        sys.exit(1)
    # The following pattern will match on some special conditions
    pet = re.compile("(.*) (.*\d+.*),(.*\d+.*) through (.*\d+.*),(.*\d+.*)")

    # for the data stream from url, we need to correct it by using decode('utf-8')
    if 'http' in args.input:
        line = response.readline().decode('utf-8').strip()
    else:
        line = response.readline().strip()
    size = int(pet.split(line)[0])

    lights = LightTester(size)

    count = 0    

    while(line):
        if count != 0:
            cmd = pet.split(line)
            lights.apply(cmd)
        if 'http' in args.input:
            line = response.readline().decode('utf-8').strip()
        else:
            line = response.readline().strip()
        if isDebug and count % 100 == 0:
            print("{} ops".format(count))
        count += 1

    print("# occupied: ", lights.count())

if __name__ == '__main__':

    main()

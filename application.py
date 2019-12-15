#!venv/bin/python3.7

import sys
import functions


if __name__ == "__main__":

    if len(sys.argv) == 2:
        current_time = str(sys.argv[1])
    else:
        functions.log("main.log", "Too many arguments supplied", True)
        sys.exit()

    if not functions.validate_time_format(current_time):
        functions.log("main.log", "Current time format supplied is incorrect. Time supplied: " + current_time, True)
        sys.exit()

    for line in sys.stdin:
        print(line)

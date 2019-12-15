#!venv/bin/python3.7

import os
import sys
import functions

if __name__ == "__main__":

    if len(sys.argv) == 2:
        current_time = str(sys.argv[1])
    else:
        functions.log("main.log", "Incorrect arguments are supplied", True)
        sys.exit()

    if not functions.validate_time_format(current_time):
        functions.log("main.log", "Current time format supplied is incorrect. Time supplied: " + current_time, True)
        sys.exit()

    if os.isatty(0):
        print("No config has been provided!")
        sys.exit()
    else:
        for line in sys.stdin:
            if functions.check_config_format(line):
                line = line.split(" ")
                minutes = line[0]
                hours = line[1]
                command = line[2]
            else:
                functions.log("unprocessed.log", "Wrong line format supplied: " + line, True)

    # check if stdin line has got correct format
        # if bad format then move to other logs for reprocessing
        # else - transform the output to correct one
    # show it to the stdout

    # sort the output by time (optional)


    # transform cron kind of look into the normal look
    # sort the array of things before the output
    # show beautiful output to stdout



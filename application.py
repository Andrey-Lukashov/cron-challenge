#!/usr/bin/python

import os
import sys
import functions

if __name__ == "__main__":
    # Check if correct arguments are provided
    if len(sys.argv) == 2:
        current_time = str(sys.argv[1])
    else:
        functions.log("main.log", "Incorrect arguments are supplied", True)
        sys.exit()

    # Validate current time provided
    if not functions.validate_time_format(current_time):
        functions.log("main.log", "Current time format supplied is incorrect. Time supplied: " + current_time, True)
        sys.exit()

    # Check if config is provided and then validate line by line
    if os.isatty(0):
        functions.log("main.log","No config has been provided", True)
        sys.exit()
    else:
        config = sys.stdin.readlines()

        if len(config) < 1 :
            functions.log("main.log", "Config file supplied is empty", True)

        for line in config:
            if functions.check_config_format(line):
                line = line.split(" ")
                minutes = line[0]
                hours = line[1]
                command = line[2]

                line = functions.transform_config_time(current_time, hours, minutes, command)

                print(line.rstrip("\n"))
            else:
                functions.log("unprocessed.log", "Wrong line format supplied: " + line, True)

    sys.exit()

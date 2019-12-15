import re
from datetime import datetime, timedelta


def log(file, message, show=False):
    """Log a message with timestamp to a specified log file

    file -- name of the log file where message will be saved
    message -- error mesage to save
    show -- flag to either show or don't show the error in the output (default = False)
    """
    try:
        f = open(file, "a+")
        error = datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " - " + message
        f.write(error + "\n")
        if show:
            print(error.rstrip("\n"))
    except IOError:
        print("Can't write to file")
    finally:
        f.close()


def validate_time_format(current_time):
    """Validate the current_time format. Must be in HH:MM format"""
    pattern = re.compile("^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$")
    if re.match(pattern, current_time):
        return True
    else:
        return False


def check_config_format(line):
    """Check if config line provided in the correct format

    line -- one line from STDIN config file
    """
    line = line.split(" ")
    if len(line) != 3:
        return False

    minutes = line[0]
    pattern = re.compile(r"\b([0-9]|[1-4][0-9]|5[0-9])\b")
    if not re.match(pattern, minutes):
        if minutes != "*":
            return False

    hours = line[1]
    pattern = re.compile(r"\b([0-9]|1[0-9]|2[0-3])\b")
    if not re.match(pattern, hours):
        if hours != "*":
            return False

    return True


def transform_config_time(current_time, hours, minutes, command):
    """Transform config time to a specific format

    current_time -- current time supplied in the arguments
    hours -- hours value from the command
    minutes -- minutes value from the command
    command -- command to be run
    """
    current_hour, current_minutes = current_time.split(":")

    hourly = False
    if hours == "*":
        hours = current_hour
        hourly = True

    if minutes == "*":
        if current_hour == hours:
            minutes = current_minutes
        else:
            minutes = "00"

    command_time = datetime.strptime(hours + ":" + minutes, '%H:%M')
    current_time = datetime.strptime(current_time, '%H:%M')

    running_day = "today"
    if command_time < current_time:
        if hourly:
            command_time = command_time + timedelta(hours=1)
            if command_time.date() == current_time.date():
                running_day = "today"
            else:
                running_day = "tomorrow"
        else:
            running_day = "tomorrow"

    return str(command_time.hour) + ":" + minutes + " " + running_day + " - " + command

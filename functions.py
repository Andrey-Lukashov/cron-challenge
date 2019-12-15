import re
from datetime import datetime


def log(file, message, show=False):
    try:
        f = open(file, "a+")
        error = datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " - " + message
        f.write(error)
        if show:
            print(error)
    except IOError:
        print("Can't write to file")
    finally:
        f.close()


def validate_time_format(current_time):
    pattern = re.compile("^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$")
    if re.match(pattern, current_time):
        return True
    else:
        return False


def check_config_format(line):
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
    current_hour, current_minutes = current_time.split(":")

    if hours == "*":
        hours = current_hour

    if minutes == "*":
        minutes = current_minutes

    command_time = datetime.strptime(hours + ":" + minutes, '%H:%M')
    current_time = datetime.strptime(current_time, '%H:%M')

    running_day = "today"
    if command_time < current_time:
        running_day = "tomorrow"

    return hours + ":" + minutes + " " + running_day + " - " + command

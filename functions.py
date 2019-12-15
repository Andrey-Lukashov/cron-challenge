import datetime
import re


def log(file, message, show):
    try:
        f = open(file, "a+")
        error = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " - " + message + "\n"
        f.write(error)
        if show:
            print(error)
    except IOError:
        print("Can't write to file")
    finally:
        f.close()


def validate_time_format(current_time):
    pattern = re.compile("^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$")
    if pattern.match(current_time):
        return True
    else:
        return False


def check_config_format(line):
    print("Lol")


def transform_config_line(line):
    print("Lol")
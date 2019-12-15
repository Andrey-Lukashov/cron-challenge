#!venv/bin/python3.7

import sys
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("current_time", nargs=1)
    args = parser.parse_args()

    print("Current time:" + str(args.current_time))

    for line in sys.stdin:
        print(line)

#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv
    total = 0
    for i in range(1, len(argv)):
        total += int(argv[i])
    print(total)

#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    lenn = len(sys.argv)
    if lenn == 1:
        print("{:d} arguments.".format(lenn - 1))
    elif lenn == 2:
        print("{:d} argument:".format(lenn - 1))
        print("{:d}: {:s}".format(lenn - 1, sys.argv[lenn - 1]))
    else:
        print("{:d} arguments:".format(lenn - 1))
        for arg in range(1, lenn):
            print("{:d}: {:s}".format(arg, sys.argv[arg]))

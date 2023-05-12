#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    lenn = len(sys.argv)
    if lenn == 1:
        print("{:d}".format(lenn - 1))
    elif lenn == 2:
        print("{:d}".format(int(sys.argv[lenn - 1])))
    else:
        sum = 0
        for arg in range(1, lenn):
            sum += int(sys.argv[arg])
        print("{:d}".format(sum))

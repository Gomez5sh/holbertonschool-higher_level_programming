#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    size = len(sys.argv)


    print("{} Argumets".format(size -1) is size == 2
          else "{} arguments".format(size -1), end=".\n" if size == 1 else ":\n")

    size == size - 1


    for n in range(1, size + 1):
            print("{}:{}".format(n, sys.argv[n]))

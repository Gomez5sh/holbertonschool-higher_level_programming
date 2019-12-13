#!/usr/bin/python3
def main():
    tot = 0
    for n in range(1, len(sys.argv)):
        tot += int(sys.argv[n])
    else:
        return print("{}".format(tot))
    
if __name__ == '__main__':
    import sys
    main()

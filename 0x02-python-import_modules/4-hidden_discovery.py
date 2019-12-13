#!/usr/bin/python3
def main():
    iterate = 0
    for n in dir(hidden_4):
        if n[0:1] != '_':
            print("{}".format(n))
if __name__ == '__main__':
    import hidden_4
    main()

#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for f in range(list_length):
        try:
            dev = my_list_1[f] / my_list_2[f]
        except (ZeroDivisionError):
            print("division by 0")
            dev = 0
        except (TypeError):
            print("wrong type")
            dev = 0
        except (IndexError):
            print("out of range")
            dev = 0
        finally:
            new_list.append(dev)
    return (new_list)

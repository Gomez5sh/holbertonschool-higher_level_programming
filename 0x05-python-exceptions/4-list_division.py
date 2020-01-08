def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for ite in range(list_length):
        try:
            dev = my_list_1[ite] / my_list_2[ite]
        except (ZeroDivisionError):
            print("division by 0")
            dev = 0
        except (ValueError, TypeError):
            print("wrong type")
            dev = 0
        except (IndexError):
            print("out of range")
            dev = 0
        finally:
            new_list.append(dev)
    return (new_list)

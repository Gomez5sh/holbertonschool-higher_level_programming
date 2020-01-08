def list_division(my_list_1, my_list_2, list_length):
    new = []
    for ite in range(list_length):
        try:
            dev = my_list_1[ite] / my_list_2[ite]
        except (ZeroDivisionError):
            print("Division by 0")
            dev = 0
        except (ValueError, TypeError):
            print("Wrong Type")
            dev = 0
        except (IndexError):
            print("Out of Range")
            dev = 0
        finally:
            new.append(dev)
    return(new)

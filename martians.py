import random
def int_validation(x):
    x = input(f"{x}")
    try:
        x = int(x)
        if x > 7 or x < 1:
            print("invalid input")
        else:
            return x
    except ValueError:
        print("wrong input")
        return 0
killometres = [711,0,0,0,1,1,0]
game = True

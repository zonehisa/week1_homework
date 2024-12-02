import random


def main():
    dice_surface_number = int(input("サイコロの面の数は？ > "))
    times_do_dice = int(input("サイコロを降る回数は？ > "))
    do_dice_list = []
    for i in range(times_do_dice):
        rand = random.randrange(1, dice_surface_number + 1)
        do_dice_list.append(rand)
    return print(do_dice_list)


if __name__ == "__main__":
    main()

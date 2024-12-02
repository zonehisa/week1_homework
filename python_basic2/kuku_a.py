a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in a:
    # print(i, end=" ")
    for j in b:
        print(i * j, end=" ")
    print("\n", end="")


def main():
    for i in range(1, 10):
        for j in range(1, 10):
            product = i * j
            print(f"{product}", end=" ")
        print("\n", end="")


if __name__ == "__main__":
    main()

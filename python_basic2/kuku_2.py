rows = int(input("行数を入力してください:"))
cols = int(input("列数を入力してください:"))

for i in range(rows):
    for j in range(cols):
        product = (i + 1) * (j + 1)
        print(f"{product:2}", end=" ")
    print("\n", end="")

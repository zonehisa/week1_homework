try:
    rows = int(input("行数を入力してください"))
    cols = int(input("列数を入力してください"))
except ValueError:
    print("整数を入力してください。")
    exit()

max_product = rows * cols
a = len(str(max_product))
print(a)
width = len(str(max_product))

for i in range(rows):
    for j in range(cols):
        product = (i + 1) * (j + 1)
        print(f"{product:{width}}", end=" ")
    print()


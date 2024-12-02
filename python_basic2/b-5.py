def calculation_total(number_list: list[int]) -> int:
    sum_number = 0
    for number in number_list:
        sum_number += number
    return sum_number


def calculation_maximum(number_list):
    max_number = number_list[0]
    for num in number_list[1:]:
        if num > max_number:
            max_number = num
    return max_number


def calculation_minimum(number_list):
    min_number = number_list[0]
    for num in number_list[1:]:
        if num < min_number:
            min_number = num
    return min_number


def calculation_average(number_list):
    sum_number = 0
    for number in number_list:
        sum_number += number
    return sum_number / len(number_list)


def main():
    number_str = input("データを入力してください(スペース区切り) > ")
    number_list = [int(x) for x in number_str.split()]
    total = calculation_total(number_list)
    maximum = calculation_maximum(number_list)
    minimum = calculation_minimum(number_list)
    average = calculation_average(number_list)
    print(f"合計値: {total}")
    print(f"最大値: {maximum}")
    print(f"最小値: {minimum}")
    print(f"平均値: {average}")


if __name__ == "__main__":
    main()

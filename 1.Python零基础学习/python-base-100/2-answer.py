def money(baseAmount):
    if(baseAmount <= 0):
        return 0
    total = 0
    list = [1000000, 600000, 400000, 200000, 100000, 0]
    rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
    for index in range(0, 6):
        if baseAmount > list[index]:
            total += (baseAmount - list[index])*rat[index]
            baseAmount = list[index]
    return total


def main():
    i = int(input('请输入利润：'))
    print(money(i))


main()


def fewDays(year, month, day):
    list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    totalDay = 0
    leap = 0
    # 判断是否闰年
    if(year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        leap = 1
    if leap == 1 and month > 2:
        totalDay += 1
    # 累加天数
    for x in range(0, 12):
        if(x < month-1):
            totalDay += list[x]

    totalDay += day
    return totalDay


def main():
    dateStr = input('请输入yyyy-mm-dd:')
    dateList = dateStr.split("-")
    year = int(dateList[0])
    month = int(dateList[1])
    date = int(dateList[2])

    print('it is the %dth day.' % fewDays(year, month, date))


main()

import datetime
from datetime import timedelta

if __name__ == '__main__':

    # 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
    print(datetime.date.today().strftime('%d/%m/%Y'))

    # 创建日期对象
    miyazakiBirthDate = datetime.date(1941, 1, 5)

    print(miyazakiBirthDate.strftime('%d/%m/%Y'))

    # 日期算术运算
    miyazakiBirthNextDay = miyazakiBirthDate + datetime.timedelta(days=1)

    print(miyazakiBirthNextDay.strftime('%d/%m/%Y'))

    # 日期替换
    miyazakiFirstBirthday = miyazakiBirthDate.replace(
        year=miyazakiBirthDate.year + 1)

    print(miyazakiFirstBirthday.strftime('%d/%m/%Y'))

    a = timedelta(days=2, hours=6)
    b = timedelta(hours=4.5)
    c = a + b

    print(c.days, '天')
    print(c.seconds, '秒')
    print(c.seconds / 3600, '分钟')
    print('共计', c.total_seconds() / 3600, '分钟')

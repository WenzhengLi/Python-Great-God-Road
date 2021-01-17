from functools import reduce
Tn = 0
Sn = []
n = int(input('n = '))
a = int(input('a = '))
for count in range(n):
    Tn = Tn + a
    a = a * 10
    Sn.append(Tn)
    print(Tn)

Sn1 = reduce(lambda x, y: x + y, Sn)  # 使用lambda简易完成函数


def add(x, y):            # 两数相加
    return x + y


Sn2 = reduce(add, Sn)
print("Sn1计算和为：", Sn1)
print("Sn2计算和为：", Sn2)

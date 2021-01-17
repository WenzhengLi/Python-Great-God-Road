s = [p for p in range(101, 201) if 0 not in [p %
                                             d for d in range(2, int(p**0.5)+1)]]
print(len(s), s)

sushu = []
for i in range(101, 201):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        sushu.append(i)
print('101-200之间的素数为：', sushu)

f = [s for s in range(101, 201) if 0 not in [s % d for d in range(2, s)]]
print(len(f), f)

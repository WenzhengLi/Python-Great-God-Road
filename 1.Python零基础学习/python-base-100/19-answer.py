for j in range(2, 1001):
    list = []
    sum = j
    for i in range(1, j):
        if j % i == 0:
            sum -= i
            list.append(i)
    if(sum == 0):
        print(j)
        print(list)

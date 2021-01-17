hei = 100
tim = 10

list = []
height = []

for i in range(1, tim+1):
    if i == 1:
        list.append(hei)
    else:
        list.append(hei*2)
    hei /= 2
    height.append(hei)
print(list)
print(height)

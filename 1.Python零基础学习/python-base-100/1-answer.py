listNum = [1, 2, 3, 4]
for i in listNum:
    for j in listNum:
        for x in listNum:
            if(i != j and i != x and j != x):
                print(str(i)+str(j)+str(x))

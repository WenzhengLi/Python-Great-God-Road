for i in range(ord('x'), ord('z')+1):
    for j in range(ord('x'), ord('z')+1):
        if i != j:
            for k in range(ord('x'), ord('z')+1):
                if (i != k) and (j != k):
                    if(i != ord('x')) and (k != ord('x')) and (k != ord('z')):
                        print('order is a -- %s\t b -- %s\tc--%s' %
                              (chr(i), chr(j), chr(k)))
# 如上方法，每个人的选择，均做出排列，然后进行选择
# 以下这种不成立，是错误的。
# order is a -- y a -- z  b -- x  b -- y  b -- z  c -- y
print('order is ', end="")
for i in range(ord('a'), ord('c')+1):
    for j in range(ord('x'), ord('z')+1):

        if (i == ord('a') and j == ord('x')):
            pass
        elif (i == ord('c') and j == ord('x')):
            pass
        elif (i == ord('c') and j == ord('z')):
            pass
        else:
            print('%s -- %s\t' % (chr(i), chr(j)), end="")

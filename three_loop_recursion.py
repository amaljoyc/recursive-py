def using_loop():
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                print i,j,k


def using_recursion(i,j,k):
    if i == 4:
        return
    elif k < 3:
        print i,j,k
        return using_recursion(i,j,k+1)
    elif j < 3:
        print i,j,k
        return using_recursion(i,j+1,1)
    else:
        print i,j,k
        return using_recursion(i+1,1,1)


if __name__ == '__main__':
    using_loop()
    print '*********************'
    using_recursion(1,1,1)
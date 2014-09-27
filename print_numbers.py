def loop(n):
    l = list()
    for x in xrange(n):
        l.append(x)
    return l


def recursion(l, n):
    if n == 0:
        return l
    else:
        l.append(n-1)
        return recursion(l, n-1)

def print_forward(n,inc):
    if n == inc:
        return n
    else:
        print inc
        return print_forward(n, inc+1)

if __name__ == '__main__':
    loop_result = loop(10)
    recursion_result = recursion(list(), 10)
    print loop_result
    print recursion_result
    print '************'
    print_forward(10, 0)
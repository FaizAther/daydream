#!/usr/bin/python

def fib_r(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fib_r(n-1) + fib_r(n-2)

def fib_r_o(n):

    list = [0,1]
    i = 2
    while(i != n+1):
	list.append(list[i-1] + list[i-2])
	#print(list[i])
	i += 1
    return list[-1]


def fib_c(n):
    import math

    return ((1.0/ (math.sqrt(5.0) ) * (
	pow(
        ((1.0 / 2.0) + math.sqrt(5.0 / 4.0)), n
	) - pow(
	((1.0 / 2.0) - math.sqrt(5.0 / 4.0)), n))
	))


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print("Usage: fib <n>")
    else:
        print("constant\t\ttime fib n={}, res={}".format(sys.argv[1], int(fib_c(int(sys.argv[1])))))
        print("optimized\t\ttime fib n={}, res={}".format(sys.argv[1], int(fib_r_o(int(sys.argv[1])))))


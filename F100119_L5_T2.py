import sys

def power(N, P):
    if P == 0:
        return 1

    return (N * power(N, P - 1))

print(power(int(sys.argv[1]), int(sys.argv[2])))
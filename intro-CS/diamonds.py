def diamond(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print('*', end='')
        print()

def antidiamond(n):
    for i in range(0,n):
        for j in range(0,n-i-1):
            print(' ', end='')
        for j in range(n-i-1,n):
            print('*', end='')
        print()

def double(n):
    for i in range(0,n):
        for j in range(0,n-i-1):
            print(' ', end='')
        for j in range(n-i-1,n+i):
            print('*', end='')
        print()

diamond(5)
print()
antidiamond(5)
print()
double(5)

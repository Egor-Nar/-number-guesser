n = int(input())
k = int(input())
num = list(range(1,n+1))
x = 0

while len(num) != 2:
    if len(num) > k:
        del num[k - 1]
        num = num[k-1:]+num[:k-1]
        print(num, len(num))
    elif len(num) == k:
        del num[k - 1]
        print(num, len(num))
    elif len(num) < k:
        if k % len(num) == 0:
            del num[ len(num)-1]
            print(num, len(num))
        elif k/len(num) < 2:
            x = len(num)
            del num[k - len(num)-1]
            num = num[k - x - 1:]+ num[:k - x - 1]
            print(num, len(num))
        elif k/len(num) > 2:
             x = len(num)
             del num[k % len(num) - 1]
             num = num[ k% x - 1:] + num[:k % x - 1]
             print(num, len(num))
if k % 2 == 0:
    print(num[0])
else:
    print(num[1])


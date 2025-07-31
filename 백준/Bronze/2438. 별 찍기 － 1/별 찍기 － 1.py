N = int(input())
if 1 <= N <= 100:
    for i in range(1,N+1):
        for j in range(i):
            print("*", end="")
        print()
else:
    print("N은 1 이상 100 이하여야 합니다.")
# 2753 윤년 구하기

y = int(input())

if ((y % 4) == 0) and ((y % 100) != 0): 
    print(1)
elif ((y % 400) == 0):
    print(1)
else:
    print(0)
    
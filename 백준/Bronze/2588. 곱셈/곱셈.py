# 2588
# 첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 
# 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.

num1 = int(input())
num2 = int(input())

num2_unit = num2 % 10
num2_ten = (num2 // 10) % 10
num2_hund = num2 // 100

line3 = num1 * num2_unit
line4 = num1 * num2_ten
line5 = num1 * num2_hund
line6 = line3 + (line4 * 10) + (line5 * 100)

print(line3)
print(line4)
print(line5)
print(line6)
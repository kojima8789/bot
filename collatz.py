def collatz(number):
    if number%2  == 0:
        number /= 2
    else:
        number = 3*number+1
    return int(number)
print('整数を入力してください')
number = int(input())

while number != 1:
    number = collatz(number)
    print(number)
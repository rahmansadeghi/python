#ماشین حساب
# دو عدد و عملگر را گرفته و محاسبه را انجام دهد

num1 = int(input("Pleas enter first number: "))
num2 = int(input("Pleas enter second number: "))
op = input("Pleas enter your operation symbol: ")

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num2 - num2)
elif op == '*':
    print(num1 * num2)
elif op == '/':
    print(num1 / num2)
else:
    print("Your operation symbol is wrong! pleas try again.")
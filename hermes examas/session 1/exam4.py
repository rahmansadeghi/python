#بیت شماری
# یک عدد دریافت کند، به باینری تبدیل کرده و تعداد یک های آنرا بشمارد




bin = bin(int(input("Pleas enter your number: ")))
co = 0
for i in bin:
    if i == '1':
        co +=1
    
print(co)
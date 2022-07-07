#شمارشاعداد اول
#را در ورودی دریافت کند به طوری که m و n برنامه ای بنویسید که دو عدد صحیح
#n ≤ m
# و در خروجی تعداد اعداد اول در بازه  [m.n] را چاپ کند



def findPrimes(x,y):
    prime_list =[]
    for i in range(x,y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2,int(i/2)+1):
                if i%j ==0:
                    break
            else:
                prime_list.append(i)
    return prime_list



FirstNum = input("Ppleas enter first number: ")
SecondNum = input("Pleas enter second number: ")

lst = findPrimes(int(FirstNum),int(SecondNum))
if len(lst) == 0:
    print("There are no prime numbers in this range")
else:
    print("You have ",len(lst) , "prime number")
    print("and that is: ", lst)

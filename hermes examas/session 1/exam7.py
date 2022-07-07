# موارد زیر در آرایه محاسبه شده و مقدار نهایی را به صورت دیکشنری بازگردانید
# ماکزیمم
#مینیمم
# میانه
#میانگین


import statistics


def calc(yourlist):
    out={
        (0, 0): max(yourlist),
        (0, 1): min(yourlist),
        (0, 2): statistics.mean(yourlist),
        (0, 3): statistics.median(yourlist)
    }
    print("MIN ", "    MAX ", "  MEAN " , "  MEDIAN ")
    
    for i in range(1):
        for j in range(4):
            print("%5.2f" % out[(i, j)], end ='   ')


    #print(out)



list1 = [5, 2, 3, 8, 10, 48]
list2 = [7 ,5 ,6 ,9 ,25 ,21 ,0 ,1]

#calc(list1)
calc(list2)
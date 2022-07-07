# اعدادی که هم شماره و هم ایندکسشان بر 3 بخش پذیر است

def find_3(templist):
    list007 = []
    
    for a in templist:
        if a == 0:
            continue
        if a % 3 == 0:
            if templist.index(a) % 3 == 0:
                list007.append(a)
                
    print(list007)





list1 = [0,3,5,9,8,1,4,6,12,18,34,6]
list2 = [8,4,6,3,15,16,21,14,18,20,27,65,12]

find_3(list1)
find_3(list2)

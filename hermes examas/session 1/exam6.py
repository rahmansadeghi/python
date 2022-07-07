#از چالش های دنیای امروزی شناسایی پیام های اسپم است.در این تمرین با توجه به فرستنده و محتوای پیام،آن را به چهار دسته زیر تقسیم می کنیم
#Not spam دسته ●
#فرستنده و محتوای پیام معتبر هستند.
#Invalid sender دسته ●
#اگر فرستنده نامعتبر ولی پایم معتبر باشد
#Invalid content دسته ●
#پیام هایی که متن نامعتبر ولی فرستنده معتبر دارند
#Invalid دسته ●
#هم فرستنده و هم پیام نا معتبر هستند
#
#
# اگر فرستنده پیام دارای نام غیر انگلیسی باشد نامعتبر است
#اگر حداقل نصف طول پیام شما از کاراکتر های حرفی استفاده نمیکرد، نامعتبر است
#



from operator import truediv


def sender_validation(userid):
    counte = 0
    for a in userid:
        if a.isalpha():
            counte +=1
    if counte <(len(userid))/2:
        return False
    else:
        return True

def message_validation(messagetxt):
    counte = 0
    for a in messagetxt:
        if a.isalpha():
            counte +=1
    if counte <(len(messagetxt))/2:
        return False
    else:
        return True
    
    


sender = input("Pleas write sender name: ")
temp_message = input("Pleas write your message: ")

a = sender_validation(sender)
b = message_validation(temp_message)


if a == True and b == True:
    print("not spam")
elif a == False and b == True:
    print("Invalid sender")
elif a == True and b == False:
    print("Invalid content")
elif a == False and b == False:
    print("Invalid")
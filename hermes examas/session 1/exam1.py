#مسئله ۱. تبدیل رادیان به درجه
#اندازه زاویه بر حسب رادیان را دریافت کرده و آن را به درجه تبدیل n برنامه ای بنویسید که در ورودی عدد صحیح
#کند و نتیجه را تا دو رقم اعشار چاپ کند.
#برای تبدیل میتوانید از رابطه زیر استفاده کنید:

# degree = radian ∗ ۱۸۰/π

import math


Rad = input("pleas enter Gradiant degree: ")
deg = (int(Rad)*(180/math.pi))
print("{:.2f}".format(deg))
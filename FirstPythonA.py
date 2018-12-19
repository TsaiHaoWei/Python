Heigh = float(input("輸入你的身高"))
Weight = int(input("輸入你的體重"))
BMI = float(Weight/(Heigh/100*Heigh/100))
print(BMI)
if BMI <18.5:
    print("過輕")
elif BMI <24.9:
    print("正常")
elif BMI < 29.9:
    print("過重")
else:
    print("超肥")
'''
intA = -1
if intA>=0:
    print("postive")
else:
    print("negative")
T= True
T= T*2
F= False
F = F*2
print(T,F)

laba = 2
print(laba>>1,laba<<1)
negA = -1
print(negA>>1,negA<<1)


'''
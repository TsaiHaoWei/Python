'''
continue , break用迴圈
for i in range(7):
    if i==3:
        continue
    if i==6:
        break
    print(i)
=============================================================
9*9成法表
for Zx in range(1,10):
    for x in range(1,10):
        print("%d*%d=%d\t"%(Zx,x,Zx*x),end="")
    print()
=============================================================    
能不換行
print("Hello",end="")
print(" Man")
=============================================================
for 迴圈
for x in range(1,10,2):
    print(x)
=============================================================    
#else if判斷
Heigh = float(input("輸入你的身高"))
Weight = int(input("輸入你的體重"))
BMI = float(Weight/(Heigh/100*Heigh/100))
print("%.2f"%BMI)
print("%.4e"%BMI)
print("%.4g"%BMI)
if BMI <18.5:
    print("過輕")
elif BMI <24.9:
    print("正常")
elif BMI < 29.9:
    print("過重")
else:
    print("超肥")
=============================================================
True非0 False 0
T= True
T= T*2
F= False
F = F*2
print(T,F)
=============================================================
左右移
laba = 2
print(laba>>1,laba<<1)
negA = -1
print(negA>>1,negA<<1)
=============================================================

'''
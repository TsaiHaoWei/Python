'''
==========================================================
int_a = 1
float_a=1.0
float_b = 2.0
int_b = 2
int_c=-2
print(int_a==float_a)
print(int_a/int_b)
print(int_a/float_b)
print(float(int_a)/int_b)
print(int_a & int_b,int_a | int_b,int_a ^ int_b,~int_c)
print(int_b//int_a)#整數除法
print(float_a**2)#幕次
==========================================================
進制轉換
Hexadecimal_converter = 17
print(format(Hexadecimal_converter,'b'), format(Hexadecimal_converter,'o'),
      format(Hexadecimal_converter,'x'))
==========================================================
字串屬性      
A_bda = "  A_bd_A  "            
print(len(A_bda),A_bda.lower(),A_bda.upper()) #長度 ,小寫 ,大寫
A_bda=A_bda.strip(); #清除空白
print(len(A_bda))
==========================================================
搜尋 陣列表示
strAry = "Hey You are perfect"
print("perfect"in strAry)
print(strAry[1:3],strAry[0:],strAry[-1])#(含 不含]
==========================================================
多行表示跟註解一樣
print(fullname)
==========================================================
跳脫
fullname = 'Tiger''\tman'
print(fullname)
==========================================================
虛數
a= 1+2j
b= 3+5j
imaginary_c=a+b
print(imaginary_c,imaginary_c.real,imaginary_c.imag)
==========================================================
strA = 'Hey' "man"
strB = strA*3
print(strA,strB)
==========================================================
交換位置
i_3 = 5
i_5 = 3
i_5,i_3=i_3,i_5
print (i_5,i_3)
==========================================================
系統長度
import sys
print(sys.maxsize)# 2的64次方 8Bytes 64Bits
==========================================================
進至表示
Bin_a = 0b11 #Binary
Oct_a = 0o11#Octal
Hex_a = 0x11#Hexadecimal
print(Bin_a,Oct_a,Hex_a)



A= input("輸入數字:" )
B= input("輸入數字:" )
a=int(A)
b=int(B)
print(a,"+",b,"=",a+b,
      "{0}-{1}={2}".format(a,b,a-b),
      "%d * %d =%d"%(a,b,a*b),
      a,"/",b,"=",(a/b),
      a,"%",b,"=",a%b)

'''

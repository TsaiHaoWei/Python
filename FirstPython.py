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

'''
Hexadecimal_converter = 17
print(format(Hexadecimal_converter,'b'), format(Hexadecimal_converter,'o'),
      format(Hexadecimal_converter,'x'))
      
A_bda = "  A_bd_A  "
print(len(A_bda),A_bda.lower(),A_bda.upper())
A_bda=A_bda.strip();
print(len(A_bda))

strAry = "Hey You are perfect"
print("perfect"in strAry)
print(strAry[1:3],strAry[0:],strAry[-1])#(含 不含]

fullname = 'Tiger''\tman'
print(fullname)

a= 1+2j
b= 3+5j
imaginary_c=a+b
print(imaginary_c,imaginary_c.real,imaginary_c.imag)

strA = 'Hey' "man"
strB = strA*3
print(strA,strB)

i_3 = 5
i_5 = 3
i_5,i_3=i_3,i_5
print (i_5,i_3)


import sys
print(sys.maxsize)# 2的64次方 8Bytes 64Bits

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

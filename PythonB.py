def addall(*a):
   print("type(a) = {0}\tlen(a) = {1}\t a[a] = {2}".format(type(a),len(a),a[0]))#<class 'tuple'>
   return sum(a)
print(addall(10,20))
print(addall(2))

'''
Name Argument
def rangeclosed(start,end):
   return range(start,end+1)
for i in rangeclosed(start=1,end=10):
   print(i)
   
def rangeclosed(start,end):
   for x in  range(start,end+1):
      yield x
print(type(rangeclosed(1,10)))#<class 'generator'>
for i in rangeclosed(start=1,end=10):
   print(i)

========================================
參數預設值
def All(id,amt=1234):
  return "%-10s%5d"%(id,amt)

id = input("輸入ID")
amt = int(input("輸入 AMT"))
print(All(id))
==============================================
Method declare
def add(a,b):
    return a+b
print(add(10,20))
===============================================
a =int(50)
sum = int(0)
while a<=100:
    if a%3 == 0 and a % 2 !=0:
            sum = sum+a
    a=a+1
print(sum)

'''
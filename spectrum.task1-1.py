a,b = input('enter two numbers separated by comma : ').split(',')
a = int(a)
b = int(b)
sum=a+b
product = (a*b)
if product>1000:
   print("the sum is :",sum)
else:
   print("the product is :",product)

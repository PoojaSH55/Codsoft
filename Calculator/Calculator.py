def add(a,b):
  return a+b
def sub(a,b):
  return a-b
def mul(a,b):
  return a*b
def div(a,b):
  return a/b

print("Operations:")
print("1. Addition")
print("2. Subtraction ")
print("3. Multiplication")
print("4. division")
choice = input("Enter your choice:")
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

if choice== '1':
   print(f"{a}+{b}={add(a,b)}")
elif choice=='2': 
   print(f"{a}-{b}={sub(a,b)}")
elif choice=='3': 
   print(f"{a}*{b}={mul(a,b)}")
elif choice=='4':
   if( b!=0):
       print(f"{a}/{b}={div(a,b)}")
   else:
       print("undefined") 

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
choice = int(input("Enter your choice:"))
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

switch(choice):
   case '1': print(a+"+"+b+"="+add(a,b))
            break;
   case '2': print(a+"-"+b+"="+sub(a,b))
            break;
   case '3': print(a+"*"+b+"="+mul(a,b))
            break;
   case '4':if( b!=0):
              print(a+"/"+b+"="+div(a,b))
            else:
            break;

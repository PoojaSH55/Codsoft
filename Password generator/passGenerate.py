import random 
import string
def generate_password(length=12):
  char=string.ascii_letters + string.digits + string.punctuation
  password=' '.join(random.choice(char)
for i in range(length))
  return password 
password=generate_password(12)
print("Your Generated Password is :", password)

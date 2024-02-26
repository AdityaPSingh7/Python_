import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
a = int(input("How many letters would you like in your password?\n")) 
b = int(input("How many symbols would you like?\n"))
c = int(input("How many numbers would you like?\n"))

# p=""
# for i in range (0, a):
#   p=p+random.choice(letters)
# for i in range (0, b):
#   p=p+random.choice(numbers)
# for i in range (0, c):
#   p=p+random.choice(symbols)
  
ps=[]
for i in range (0, a):
  ps.append(random.choice(letters))
for i in range (0, b):
  ps.append(random.choice(numbers))
for i in range (0, c):
  ps.append(random.choice(symbols))
  
random.shuffle(ps)

p=""
for i in ps:
  p=p+i
print(p)

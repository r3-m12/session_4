a = 34 #variable 1 
b = 200 #variable 2 
c = "bonjours" #variable 3 
is_on = False
i = 0 
while i < 6:
  i += 1
  if is_on:
    print("Allo")
  else:
    print("Bonjours")
  is_on = not is_on
print(c)
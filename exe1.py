##Write a python function that takes a name as argument and prints it
def print_this_name(name):
  print("Name:",name)

print_this_name("Radha")


###Write a python function that takes a string as argument and prints whether it is uppercase or lowercase
def upper_or_lower(word):
  if word.isupper():
    print ("It is upper case")
  else:
    print ("It is lower case")
upper_or_lower("AFGJHJTYUTGU")
upper_or_lower("asddffghfrsds")


####Write a list comprehension that capitalises every letter in the word 'smogtether
capital=[x.upper() for x in "smogetether"]
capstring=''.join(capital)
print(capstring)

###Write a generator function that alternates between odd and even
def odd_or_even(n):
  while True:
    n+=1
    if n%2 :
      yield "Odd"
    else:
      yield "Even"
  

odd_or_even(45)
  

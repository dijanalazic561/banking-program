from parsers import parse
import random
user_input=input("Enter  upper,lower bound(1-10) separated by comma")
parsed=parse(user_input)
rand=random.randint(parsed["lower_bound"],parsed['upper_bound'])
print(rand)
from converters import convert
from parsed import parse

feet_inches = input("Enter feet and inches followed by space")

parsed= parse(feet_inches)
result= convert(parsed["feet"], parsed["inches"])
print(f"{parsed["feet"]}feet and {parsed["inches"]}is equal to {result}")
if result<1:
      print("Kid is to small")
else:
     print("Kid can use slide")
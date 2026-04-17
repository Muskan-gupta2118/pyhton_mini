#Task_1 :safe division utility
nume=int(input("Enter the number for numerator"))
deno=int(input("Enetr the number for denominator"))
try:
  print(f"your quotient is {nume/deno}") 
except ZeroDivisionError as exception:
  print(exception)
else:
  print("Operation completed")    

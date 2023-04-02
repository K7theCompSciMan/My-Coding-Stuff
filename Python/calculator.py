#The following functions are the operations that the calculator performs

#This function adds the 2 inputs and displays the equation.
def addition():
  sum = num1 + num2
  print(f"{num1} + {num2} = {sum}")

#This function subtracts the 2 inputs and displays the equation.
def subtraction():
  dif = num1 - num2 
  print(f"{num1} - {num2} = {dif}")

#This function multiplies the 2 inputs and displays the equation
def multiplication():
  pro = num1 * num2
  print(f"{num1} * {num2} = {pro}")

#This function divides the 2 inputs and displays the equation
def division():
  quo = num1 / num2
  print(f"{num1} / {num2} = {quo}")

#This function is used to truncate the 2 inputs and display the equation
def truncation():
  ans = num1 // num2
  print(f"{num1} // {num2} = {ans}")

#This function asks for an input, checks if it has alpha characters and returns it to the main program
def inp1():
  while True:
    num1 = input("Input a first number: ")
    if num1.isalpha() == False: #This checks if the input is all digits then produces an answer.
      num1 = float(num1)
      break
    else:
      print("\nInvalid Entry. Try again. \n")
  return num1

#This function asks for the second input, checks for alpha characters, and return the value to the main program. 
def inp2():
  while True:
    num2 = input("Input a second number: ")
    if num2.isalpha() == False: #This checks if the input is all digits then produces an answer.
      num2 = float(num2)
      break
    else:
      print("\nInvalid entry. Try again \n")
  return num2

print("Welcome to our 5-function calculator! \n")

#This loops the entire program so that the calculator can be used multiple times.
while True:
  num1 = inp1()
  num2 = inp2()
#This loop asks for an operation and resets if the input was not desired.
  while True:
    opp = input("Select an operation: \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Truncation \n")
    if opp == "1":
      addition()
      break
      
    elif opp == "2":
      subtraction()
      break
      
    elif opp == "3":
      multiplication()
      break

#This algorithm ensures that the calculator does not divide by zero by checking if the second input was zero if the operation chose was division.
    elif opp == "4":
      if num2 != 0:
        division()
        break
      else:
        print("Divide by Zero Error! Try Again \n")
        num2 = inp2()
        
    elif opp == "5":
      truncation()
      break
      
    else:
      print("Invalid entry. Try again!\n")
      
  #This loop ensures that the person can use the calculator multiple times.
  while True:    
    again = input("Do you want to do another calculation? Y or N \n")
  
    if again.lower() == "n" or again.lower() == "no":
      print("Thank You for using this calculator.\n")
      break
      
    elif again.lower() == "y" or again.lower() == "yes":
      break
    else:
      print("Invalid Entry! Try Again.")      
  if again.lower() == "n" or again.lower() == "no":
    break
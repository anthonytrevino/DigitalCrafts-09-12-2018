def add(firstNumber, secondNumber):
    return firstNumber + secondNumber

def subtract(firstNumber, secondNumber):
    return firstNumber - secondNumber

def multiply(firstNumber, secondNumber):
    return firstNumber * secondNumber

def divide(firstNumber, secondNumber):
    return firstNumber / secondNumber

print("What would you like to do?")
print("Addition")
print("Subtraction")
print("Multiplication")
print("Division")

operation = input("Select an Operation. ")

firstNumber = int(input("Enter first number: "))

secondNumber = int(input("Enter second number: "))



if operation == "Addition":
    result = add(firstNumber,secondNumber)
    print(f"{firstNumber} + {secondNumber} = {result}")


elif operation == "Subtraction":
    result = subtract(firstNumber,secondNumber)
    print(f"{firstNumber} - {secondNumber} = {result}")

elif operation == "Multiplication":
    result = multiply(firstNumber,secondNumber)
    print(f"{firstNumber} * {secondNumber}, {result}")

elif operation == "Division":
    result = divide(firstNumber,secondNumber)
    print(f"{firstNumber} / {secondNumber}, {result}")

#calculator({0}{1}{2}.format())









#def calculator():

 # int(input1("What is your first number?"))
  #input2("What math operation will you perform?")
  #if(+)
    #    input1 + input2

     # else:(-)
    #    input 1 - input2

     # else:(*)
    #    input 1 * input2

     # else:(/)
    #    input1 % input2



#int(input3("What is your second number?"))

def checker(number):

 if(number % 3  == 0 and number % 5 ==0):
      print("FizzBuzz")

 elif(number % 5 == 0):
      print("Buzz")

 elif(number % 3 == 0):
      print("Fizz")

number = int(input("Enter a number"))
checker(number)

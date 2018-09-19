num=int(input("Enter a number: "))

if num > 1:

    for i in range(2,num):
        if (num % i) == 0 :
            print("This number is not prime. ")
            break
    else:
            print("This number is prime. ")
else:
    print(num,"is not a prime number")

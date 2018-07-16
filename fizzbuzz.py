filename = "fizzbuzz.txt"
num = 0
number = int(input("What is your number?:"))
my_file = open("filename", "W+")

for num in range(1, number):
    if num%3==0 and num%5==0:
        print ("Fizzbuzz", number)
        my_file.write("Fizzbuzz"+ str(number))
    elif num%5==0:

        print("buzz", number)
    elif num%3==0:
        print("fizz", number)
    else:
     print("FizzBuzz", number)



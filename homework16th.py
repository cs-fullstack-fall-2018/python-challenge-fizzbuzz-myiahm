# try:
#     for i in ['a', 'b', 'c']:
#         print(i ** 2)
# except:
#  print("type error occured ")

# x= 5
# y = 0
#
#
# try:
#     z = x/y
#     print(z)
# except:
#     print("zero division error ")
# finally:
#     print("All done")
import sys
def ask():
    numberToBeSquared = input("interger")

    try:
        print("Thank you, you number squared is: ", int(numberToBeSquared)**2)
    except:
        print("An error occurred! Please try again!: ")
ask()
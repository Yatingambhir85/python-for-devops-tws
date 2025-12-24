#Functions

env = input("Enter the environment: ") #taking input from the user
print ("The environment is", env)

def sum_of_num(): #function definition
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    sum = a + b
    print("Sum is:", sum)

if env =='prod':
    sum_of_num()  #function calling

def take_backup():
    print("Backup script started...")

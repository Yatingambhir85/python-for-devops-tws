 #snake case in python: my_file, check_env, hello_dosto
# camel case: myFile, checkEnv, helloDosto

#get the environment from user and print it

env = input("Enter the environment: ") #taking input from the user

print("The environment is", env)

#conditional statements
if env =='prod':
    print("Dont deploy on Friday!")
elif env == 'stg':
    print("Take backup & test well!")
else:
    print ("Safe to deploy any day!")
#type-casting example - conversion of one datatype to another datatype
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: ")) 

print("Data type of a is", type(a))
print("Addition of a & b is", a + b)  # this will concatenate as both a & b are string type
print("Multiplication of a & b is", a * b)  # this will repeat string b, a times if a is integer

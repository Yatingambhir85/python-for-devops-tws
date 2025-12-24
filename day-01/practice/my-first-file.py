#hello dosto
print('hello dosto')

#variables & constants

output = 'yes' #variable assignment
output = 'no'  # re-assigning value

a = 100 #a is variable and 100 is constant
env = 'dev' #env is variable and 'dev' is constant
# = is assignment operator
# + - * / % are arithmetic operators

# data types
#integers - 1, 2 , 4
#float - 1.5 , 2.6, -2.3
#boolean - True(1) , False(0)
#String - 'hello', "dosto", 'my name is'

print(type(a))  # to check data type of variable
print(type(env))

# a = 20.3
# b = 30.7

a = eval(input('Enter value for a: '))  # input function to take user input
b = eval(input('Enter value for b: '))

z = a * b
print("Multiplication of a & b is",z)
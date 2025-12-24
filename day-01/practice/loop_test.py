for i in range(5):
    env = input("Enter the environment: ") #taking input from the user
    if env =='prod':
        print("Dont deploy on Friday!")
    elif env == 'stg':
        print("Take backup & test well!")
    else:
        print ("Safe to deploy any day!")
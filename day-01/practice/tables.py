
choice = input("Enter the choice {press q to quit}: ")
while choice != 'q':
    num = int(input("Enter a number: "))
    print("Multiplication Table for", num)
    for i in range(10):
        print(f"{num} x {i+1} = {num*(i+1)}")
    choice = input("Enter the choice {press q to quit}: ")
    if choice == 'q':
        break
# while suraj =='chand':
#     print("Hello Dosto")
#     break

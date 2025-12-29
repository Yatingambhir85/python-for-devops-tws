import requests

url ='https://jsonplaceholder.typicode.com/todos/1'

response = requests.get(url=url)

print(response.status_code)
print(dir(response))
print(response.json())
print(type(response.json()))
for key, value in response.json().items():
    print(key, ":", value)

for key,value in response.json().items():
    if key == 'completed' and value == False:
        print("Task is not completed")
    elif key == 'completed' and value == True:
        print("Task is completed")

for key,value in response.json().items():
    if key == 'userId' and value in [100,200,300]:
        print("User is not valid")
    else:
        print("User is valid")
        break
    
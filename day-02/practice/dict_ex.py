info ={
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "occupation": "Engineer",
    "favourite_colors": ["blue", "green", "red"],
    "married": False
}

print(info["name"])  # Accessing the value associated with the key "name"
print(info["favourite_colors"][1])  # Accessing the second favorite color
print("I love ",info.get("favourite","black"))  # Using get method with a default value

info.update({"favourite country": "USA"})  # Adding a new key-value pair
print(dir(info))  # Displaying all attributes and methods of the dictionary object

#Iterating through the dictionary
for key,value in info.items():
    print(key, ":", value)  # Iterating through the dictionary and printing key-value pairs

days = {'saturday','sunday','monday','tuesday','wednesday','thursday','friday'}
print(type(days))
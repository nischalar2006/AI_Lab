



# arithmaic operatrion
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

print(f"Addition of {a} and {b} : {a + b}")
print(f"Multiplication of {a} and {b} : {a * b}")
print(f"Difference of {a} and {b} : {a - b}")
print(f"Division of {a} by {b} : {a / b}")


# even /odd numbers 
num = int(input("Enter a number: "))


if num % 2 == 0:
    print(f"{num} is an Even number.")
else:
    print(f"{num} is an Odd number.")





#  dictionary
student = {"name": "Alice", "age": 20, "course": "Python"}


print(student["name"])      
print(student.get("age"))  


student["age"] = 21          
student["city"] = "London"   


for key, value in student.items():
    print(f"{key}: {value}")







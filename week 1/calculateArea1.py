import moduleArea

retry = "y"
while retry == "y":

    print("""
    Type of Shape: 
    1. Circle
    2. Triangle
    3. Square
    4. Trapezium
    """)

    shape = input("enter type of shape: ")

    if shape == "1":
        moduleArea.circle()
    elif shape == "2":
        moduleArea.triangle()
    elif shape == "3":
        moduleArea.square()
    elif shape == "4":
        moduleArea.trapezium()
    else:
        print("not a choice!")

    retry = input("continue? y/n -->")
    if retry == "y":
        continue
    else:
        break

    
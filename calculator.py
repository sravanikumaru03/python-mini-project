def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b == 0:
        return "cannot divide by zero"
    return a / b
while True:
    print("\n.....calculator.....")
    print("1.Add")
    print("2.subtract")
    print("3.multiplication")
    print("4.division")
    print("5.exit")
    choice = input("enter choice(1-5):")
    if choice == "5":
        print("exiting calculator...")
        break
    if choice not in['1','2','3','4','5']:
        print("invalid choice....")
        continue
    a = float(input("enter number1:"))
    b = float(input("enter number2"))
    if choice == "1":
        print("result:",add(a,b))
    elif choice == "2":
        print("result:",subtract(a,b))
    elif choice == "3":
        print("result:",multiply(a,b))
    elif choice == "4":
        print("result:",divide(a,b))









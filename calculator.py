def main():
    num1 = int(input("give me a number: "))
    num2 = int(input("give me another number: "))

#adding function
def add(a, b):
    output = a + b
    return output

#subtracting function
def subtract(a, b):
    output = a - b
    return output

#multiplication function
def multiply(a, b):
    output = a * b
    return output

#division function
def divide(a, b):
    if b == 0:
        return "dividing by zero error"
    else:
        output = a / b
        return output


if __name__ == "__main__":
    main()
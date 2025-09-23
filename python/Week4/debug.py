def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    averageRt = average**.5
    return averageRt

a = float(input("enter a number: "))
b = float(input("enter a second number: "))
c = float(input("enter a third number: "))
numbers_list = [a, b, c]


# The function call where we'll examine the variables
result = calculate_average(numbers_list)

print(f"The square root of the average is: {result}")
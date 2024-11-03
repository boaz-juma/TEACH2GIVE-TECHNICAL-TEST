"""Write a program that takes an integer as input and returns an integer with
reversed digit ordering.
Examples:
For input 500, the program should return 5.
For input -56, the program should return -65.
For input -90, the program should return -9.
For input 91, the program should return 19."""


def reverse_number(num):
    is_negative = num < 0
    reversed_num = int(str(abs(num))[::-1])
    return -reversed_num if is_negative else reversed_num

print(reverse_number(500))  # Output: 5
print(reverse_number(-56))  # Output: -65
print(reverse_number(-90))  # Output: -9
print(reverse_number(91))   # Output: 19
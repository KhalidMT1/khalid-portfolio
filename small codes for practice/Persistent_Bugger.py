# Practice difficulty: 6 kyu
# Write a function, persistence,
# that takes in a positive parameter num and returns its multiplicative persistence,
# which is the number of times you must multiply the digits in num until you reach a single digit.

def persistence(n):
    counter = 0
    while n > 9:
        number_string = str(n)
        mult_result = 1
        for i in number_string:
            mult_result *= int(i)
        print(f"Iteration Number {counter} Result = {mult_result}")
        counter += 1
        n = mult_result
    return counter


print(f"Total Number of iterations : {persistence(999)}")
print(f"Total Number of iterations : {persistence(39)}")
print(f"Total Number of iterations : {persistence(4)}")
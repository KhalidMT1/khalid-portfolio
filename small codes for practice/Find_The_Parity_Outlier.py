# Practice:
# You are given an array (which will have a length of at least 3, but could be very large)
# containing integers. The array is either entirely composed of
# odd integers or entirely composed of even integers except for a single integer N.
# Write a method that takes the array as an argument and returns this "outlier" N.

def find_outlier(integers):
    even_list = []
    odd_list = []
    for i in integers:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)

    if len(even_list) > len(odd_list):
        return odd_list[0]
    else:
        return even_list[0]

    # Another neat way of solving the problem:
    # odds = [x for x in int if x % 2 != 0]
    # evens = [x for x in int if x % 2 == 0]
    # return odds[0] if len(odds) < len(evens) else evens[0]


print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
#Given an array of integers, find the one that appears an odd number of times.

#There will always be only one integer that appears an odd number of times.

def find_it(seq):
    for i in seq:
        value = seq.count(i)
        if value % 2 != 0:
            return i


print(find_it([1,1,1,1,1,1,10,1,1,1,1]))
print(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]))
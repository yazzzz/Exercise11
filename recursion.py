# Multiply all the elements in a list
def multiply_list(l):
    if len(l) == 1:
        return l.pop()
    else:
        item = l.pop()
        return item * multiply_list(l)

# print multiply_list([1, 2, 3, 4, 5])

# Return the factorial of n
def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n-1) * n

# print factorial(5)

# Count the number of elements in the list l
def count_list(l):
    if len(l) == 1:
        return 1
    else:
        l.pop()
        return count_list(l) + 1

#print len([1, 2, 3, 4, 5, 6])
#print count_list([1, 2, 3, 4, 5, 6])

# Sum all of the elements in a list
def sum_list(l):
    if len(l) == 1:
        return l.pop()
    else:
        item = l.pop()
        return item + sum_list(l)

#print sum_list([1, 2, 3, 4, 5])

# Reverse a list without slicing or loops
def reverse(l):
    #resultlist = [] #part of alternative solution noted below
    if len(l) == 1:
        return l
    else:
        item = l.pop(0)
        return [item] + reverse(l)
        # long alt also works below
        # resultlist = reverse(l)
        # resultlist.append(item)
        #return resultlist

print reverse([1,2,3,4])

# Fibonacci returns the nth fibonacci number. The nth fibonacci number is
# defined as fib(n) = fib(n-1) + fib(n-2)
def fibonacci(n):
    pass

# Finds the item i in the list l.... RECURSIVELY
def find(l, i):
    if i == 0:
        return l[0]
    else:
        l.pop(0)
        return find(l, i-1)
        
#print find(["a","b","c","d","e"], 4)

# Determines if a string is a palindrome
def palindrome(some_string):
    if len(some_string) == 1 or len(some_string) == 0:
        return True
    else:
        first_value = some_string[0]
        last_value = some_string[-1]
        if first_value != last_value:
            return False
        else:
            return palindrome(some_string[1:-1])

print palindrome("toot")    

# Given the width and height of a sheet of paper, and the number of times to fold it, return the final dimensions of the sheet as a tuple. Assume that you always fold in half along the longest edge of the sheet.
def fold_paper(width, height, folds):
    return (0, 0)

# Count up
# Print all the numbers from 0 to target
def count_up(target, n):
    return

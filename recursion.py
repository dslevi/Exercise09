# Multiply all the elements in a list
def multiply_list(l):
    if l == []:
        return 1
    return l[0] * multiply_list(l[1:])

# Count the number of elements in the list l
def count_list(l):
    if l == []:
        return 0
    return 1 + count_list(l[1:])

# Sum all of the elements in a list
def sum_list(l):
    if l == []:
        return 0
    return l[0] + sum_list(l[1:])

# Reverse a list without slicing or loops
def reverse(l):
    if len(l) == 0:
        return []
    num = l.pop(0)
    new_l = reverse(l)
    new_l.append(num)
    return new_l

# Fibonacci returns the nth fibonacci number. The nth fibonacci number is
# defined as fib(n) = fib(n-1) + fib(n-2)
def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)

# Finds the item i in the list l.... RECURSIVELY
def find(l, i):
    if l == []:
        return None
    if l[0] == i:
        return l[0]
    return find(l[1:], i)

# Determines if a string is a palindrome
def palindrome(some_string):
    if some_string == "":
        return True
    char = some_string[-1]
    if some_string[0] != char:
        return False
    return palindrome(some_string[1:-1])

# Given the width and height of a sheet of paper, 
# and the number of times to fold it, return the final dimensions of the sheet as a tuple. 
# Assume that you always fold in half along the longest edge of the sheet.
def fold_paper(width, height, folds):
    if folds == 0:
        return (width, height)
    if width > height:
        width /= 2
    else:
        height /= 2
    return fold_paper(width, height, folds-1)

# Count up 
# Print all the numbers from 0 to target
def count_up(target, n):
    print n
    if n == target:
        return
    return count_up(target, n + 1)

def factorial(i):
    if i == 0:
        return 1
    return i * factorial(i-1)

print factorial(3)
# Define a procedure, print_multiplication_table,
# that takes as input a positive whole number, and prints out a multiplication,
# table showing all the whole number multiplications up to and including the
# input number. The order in which the equations are printed matters.

def print_multiplication_table(n):
    a = 1 #any randon number a
    while a <= n:
        b = 1 #any random b. a and b are given 1 because multiplication tables always start with 1*1
        while b <= n:
            print str(a) + ' * ' + str(b) + ' = ' + str(a * b)
            b += 1 #this is similar to b = b + 1
        a += 1 #a = a + 1


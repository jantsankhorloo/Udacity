# Write a Python procedure fix_machine to take 2 string inputs
# and returns the 2nd input string as the output if all of its
# characters can be found in the 1st input string and "Give me
# something that's not useless next time." if it's impossible.

def fix_machine(debris, product):
    i = 0
    while i < len(product):
        if debris.find(product[i]) == -1:
            return "Give me something that's not useless next time."
            break
        i += 1
    return product

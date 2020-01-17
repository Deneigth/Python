from utill.input_error_handling_utill import input_int_with_constraint  

def print_herringbone(height):
    for i in range(1, height, 2):
        print((i * '*').center(height))


print_herringbone(input_int_with_constraint('Please enter a value, it should be > 3:\n', 3))

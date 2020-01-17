from utill.input_error_handling_utill import input_int_with_constraint

def print_aproximate_sequence(depth):
    tmp = 1/2
    for i in range(2, depth):
        tmp += 1/2**i
    print(tmp)

print_aproximate_sequence(input_int_with_constraint('Please enter a value, it should be > 1:\n', 1))

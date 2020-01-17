def input_int_with_constraint(prompt, constraint):
    while True:
        try:
            value = int(input(prompt))
            if value <= constraint:
                raise ValueError
            break
        except ValueError:
            print('Oops! That was no valid number...')
            prompt = 'Try again...:\n '
    return value
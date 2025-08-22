def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}
calculated_num = 0


def calculate(first_num, operation, second_num):
    if operation in operations:
        return operations[operation](first_num, second_num)
    else:
        return 'Invalid entry'


calc_on = True
while calc_on:
    print('Welcome to the calculator')
    first_number = float(input('What is your first number?'))

    for symbol in operations:
        print(symbol)

    chosen_operation = input('What operation do you choose?')
    second_number = float(input('What is your second number?'))

    calculated_num = calculate(first_number, chosen_operation, second_number)
    print(calculated_num)
    continue_or_restart = input(
        f'Type "y" to continue calculating with {calculated_num}, or type "n" to start a new calculation: ').lower()
    if continue_or_restart == 'n':
        continue
    while continue_or_restart == 'y':
        first_number = calculated_num
        chosen_operation = input('What operation do you choose?')
        second_number = float(input('What is your second number?'))
        calculated_num = calculate(first_number, chosen_operation, second_number)
        print(calculated_num)
        continue_or_restart = input(
            f'Type "y" to continue calculating with {calculated_num}, or type "n" to start a new calculation: ').lower()
        if continue_or_restart == 'n':
            break
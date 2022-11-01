#

from stack import Stack

#


def operator_precedence(input_operator):
    """The function returns the precedence of the operators such that the lower the number the higher precedence."""
    first_precedence = ('*', '/', '%')
    second_precedence = ('+', '-')
    if input_operator in first_precedence:
        return 1
    elif input_operator in second_precedence:
        return 2


s = Stack()
output_string = []

input_string = input("Please enter the infix expression: ")
for c in input_string:
    if 37 <= ord(c) <= 47:
        if s.is_empty():
            s.push(c)
        else:
            # The precedence is higher for the lower number.
            if operator_precedence(s.peek()) <= operator_precedence(c):
                output_string.append(s.pop())
                s.push(c)
            else:
                s.push(c)
    else:
        output_string.append(c)
# Empty the stack.
while not s.is_empty():
    output_string.append(s.pop())


print(output_string)

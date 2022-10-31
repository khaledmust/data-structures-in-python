from stack import Stack

s = Stack()


def parentheses_checker(input_string):
    if len(input_string) == 0:
        print("Please enter a non empty string.")
    for c in input_string:
        if s.is_empty() and c == '(':
            s.push(c)
        elif s.is_empty():
            print("The input string is invalid")
            return
        elif c == s.peek():
            s.push(c)
        else:
            s.pop()

    if s.is_empty():
        return True
    else:
        return False


usrStr = input("Please enter your parentheses string: ")
if parentheses_checker(usrStr):
    print("The parentheses string is balanced.")
else:
    print("The parentheses string is NOT balanced.")


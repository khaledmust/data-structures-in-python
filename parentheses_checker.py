from stack import Stack

s = Stack()


def parentheses_checker(input_string):
    if len(input_string) == 0:
        print("Please enter a valid string.")
    else:
        for i in range(len(input_string)):
            if s.is_empty():
                s.push(input_string[i])
            else:
                tmp = s.peek()
                if tmp == input_string[i]:
                    s.push(input_string[i])
                else:
                    s.pop()
        if s.is_empty():
            return print("The string is balanced.")
        else:
            return print("The string is not balanced.")


usrStr = input("Please enter your parentheses string: ")
parentheses_checker(usrStr)

from stack import Stack

s = Stack()

input_num = int(input("Enter your base 10 number: "))

while input_num != 0:
    s.push(input_num % 2)
    input_num //= 2

output_string = []
while not s.is_empty():
    output_string.append(s.pop())

output_string = [str(x) for x in output_string]
output_string = "".join(output_string)

print(output_string)
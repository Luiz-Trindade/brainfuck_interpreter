# Simple BrainFuck Interpreter in Python.
# Made By: Luiz Gabriel Magalhães Trindade.
# That Program is Distributed By The GPL3 License.
# GPL3 License Link: https://www.gnu.org/licenses/gpl-3.0.en.html#license-text

from sys import argv, stdout

memory = [0]
ptr = int(0)

program = ""

program_name = str(argv[1])
if "+" in program_name or "-" in program_name:
    program = program_name
else:
    with open(program_name, "r") as f:
        content = f.readlines()
        for i in content:
            program += i.strip()

length = len(program)
counter = int(0)

loop_stack = []

while counter < length:
    memory.append(0)
    command = program[counter]

    if command == "+":
        memory[ptr] += 1
        #if memory[ptr] > 255:
        #    memory[ptr] = 0

    elif command == "-":
        memory[ptr] -= 1
        #if memory[ptr] < 0:
        #    memory[ptr] = 255

    elif command == ".":
        value = memory[ptr] % 256
        stdout.write(chr(value))

    elif command == ">":
        ptr += 1

    elif command == "<":
        ptr -= 1

    elif command == "[":
        loop_stack.append(counter)

    elif command == "]":
        if memory[ptr] == 0:
            loop_stack.pop()
        else:
            counter = loop_stack[-1]

    elif command == ",":
        content = input()
        char = content[0]
        memory[ptr] = ord(char)
        ptr += 1

    counter += 1

print("")

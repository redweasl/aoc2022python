# This is the fifth day of Advent of Code 2022.

# Delicate shipping crate process. Given instructions to move the crates.
# Output what crates are on top of each stack.

def cleaning():
    part_one()
    part_two()


def part_one():

    with open('crates.txt', 'r') as f:
        true = 1
        while true:
            next_line = f.readline().strip()
            if next_line == '': break
            previous_line = next_line

        # Obtain the line that specifies the number of stacks needed.
        num_stacks = int(previous_line[len(previous_line) - 1])
        stacks = []
        i = 0
        while i < num_stacks:
            stacks.append([])
            i += 1
        f.seek(0)

        # Read the crates again. This time, append characters to their appropriate stack.
        next_line = f.readline()
        while true:
            previous_line = next_line
            next_line = f.readline()
            if next_line == '\n': break
            i = 1
            j = 0
            while i < len(previous_line):
                if ord(previous_line[i]) != 32:
                    stacks[j].append(previous_line[i])
                j += 1
                i += 4

        # Reverse the order of the stacks to make them in the proper order
        correct_stacks = []
        i = 0
        while i < num_stacks:
            correct_stacks.append([])
            while len(stacks[i]) != 0:
                correct_stacks[i].append(stacks[i].pop())
            i += 1

        # print(f'PART ONE TEST: Starting state of the crates:\n')
        # i = 0
        # while i < len(correct_stacks):
        #     print(f'{correct_stacks[i]}\n')
        #     i += 1

        # Once the stacks are made, perform the instructions.
        num_moves = 0
        starting_stack = 0
        ending_stack = 0

        while true:
            next_line = f.readline().strip()
            if next_line == '': break

            # Obtain the numbers to perform the instruction.
            # starting and ending stack indices are zero-indexed, so the value needs to be decremented by 1.
            partition = next_line.split(" ")
            num_moves = int(partition[1])
            starting_stack = int(partition[3]) - 1
            ending_stack = int(partition[5]) - 1

            # Perform the instruction
            for i in range(num_moves):
                correct_stacks[ending_stack].append(correct_stacks[starting_stack].pop())
            # print(f'PART ONE TEST: Move {num_moves} from {starting_stack + 1} to {ending_stack + 1}\n')
            # i = 0
            # while i < len(correct_stacks):
            #     print(f'{correct_stacks[i]}\n')
            #     i += 1

        top_crates_string = []
        for i in correct_stacks:
            if len(i) > 0:
                top_crates_string.append(i.pop())

        print(f'PART ONE: The top crates string for the CrateMover9000 is {top_crates_string}\n')


# Solution is very similar to part 1.
# The only difference is the order when moving crates needs to be retained.
# Therefore, a dummy stack is used in the middle when transferring crates. This keeps the order.

def part_two():

    with open('crates.txt', 'r') as f:
        true = 1
        while true:
            next_line = f.readline().strip()
            if next_line == '': break
            previous_line = next_line

        # Obtain the line that specifies the number of stacks needed.
        num_stacks = int(previous_line[len(previous_line) - 1])
        stacks = []
        i = 0
        while i < num_stacks:
            stacks.append([])
            i += 1
        f.seek(0)

        # Read the crates again. This time, append characters to their appropriate stack.
        next_line = f.readline()
        while true:
            previous_line = next_line
            next_line = f.readline()
            if next_line == '\n': break
            i = 1
            j = 0
            while i < len(previous_line):
                if ord(previous_line[i]) != 32:
                    stacks[j].append(previous_line[i])
                j += 1
                i += 4

        # Reverse the order of the stacks to make them in the proper order
        correct_stacks = []
        i = 0
        while i < num_stacks:
            correct_stacks.append([])
            while len(stacks[i]) != 0:
                correct_stacks[i].append(stacks[i].pop())
            i += 1

        # print(f'PART ONE TEST: Starting state of the crates:\n')
        # i = 0
        # while i < len(correct_stacks):
        #     print(f'{correct_stacks[i]}\n')
        #     i += 1

        # Once the stacks are made, perform the instructions.
        num_moves = 0
        starting_stack = 0
        ending_stack = 0

        while true:
            next_line = f.readline().strip()
            if next_line == '': break

            # Obtain the numbers to perform the instruction.
            # starting and ending stack indices are zero-indexed, so the value needs to be decremented by 1.
            partition = next_line.split(" ")
            num_moves = int(partition[1])
            starting_stack = int(partition[3]) - 1
            ending_stack = int(partition[5]) - 1

            # Perform the instruction
            # THE DIFFERENCE FROM PART ONE IS LOCATED HERE--------------------------------------------------------------
            # Create the dummy stack. Transfer crates to the dummy stack, then to the destination.
            dummy_stack = []

            for i in range(num_moves):
                dummy_stack.append(correct_stacks[starting_stack].pop())
            for i in range(num_moves):
                correct_stacks[ending_stack].append(dummy_stack.pop())

            # print(f'PART TWO TEST: Move {num_moves} from {starting_stack + 1} to {ending_stack + 1}\n')
            # i = 0
            # while i < len(correct_stacks):
            #     print(f'{correct_stacks[i]}\n')
            #     i += 1

        top_crates_string = []
        for i in correct_stacks:
            if len(i) > 0:
                top_crates_string.append(i.pop())

        print(f'PART TWO: The top crates string for the CrateMover9001 is {top_crates_string}\n')


cleaning()

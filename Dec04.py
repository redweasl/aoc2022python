# This is the fourth day of Advent of Code 2022.

# Elves are assigned cleaning tasks, but have overlaps!
# Elves pair up with their cleaning tasks. Find how many pairs have complete overlaps.

def cleaning():
    part_one()
    part_two()


def part_one():
    num_total_overlap_pairs = 0
    start_elf_one = 0
    end_elf_one = 0
    start_elf_two = 0
    end_elf_two = 0

    with open('cleaning_assignments.txt', 'r') as f:
        true = 1
        while true:
            next_line = f.readline().strip()
            if next_line == '': break

            # Traverse through the line and extract values
            partition = next_line.partition("-")
            start_elf_one = int(partition[0])
            partition = partition[2].partition(",")
            end_elf_one = int(partition[0])
            partition = partition[2].partition("-")
            start_elf_two = int(partition[0])
            end_elf_two = int(partition[2])

            # Check if one of the sections and elf is cleaning completely overlaps the other
            if (start_elf_one <= start_elf_two and end_elf_one >= end_elf_two) or (
                    start_elf_one >= start_elf_two and end_elf_one <= end_elf_two):
                num_total_overlap_pairs += 1

    print(f'PART ONE: The number of completely overlapping pairs is {num_total_overlap_pairs}.\n')


# Solution is very similar to part 1.
# The only difference is the conditions needed to increment the number of overlapping pairs.

def part_two():
    num_overlap_pairs = 0
    start_elf_one = 0
    end_elf_one = 0
    start_elf_two = 0
    end_elf_two = 0

    with open('cleaning_assignments.txt', 'r') as f:
        true = 1
        while true:
            next_line = f.readline().strip()
            if next_line == '': break

            # Traverse through the line and extract values
            partition = next_line.partition("-")
            start_elf_one = int(partition[0])
            partition = partition[2].partition(",")
            end_elf_one = int(partition[0])
            partition = partition[2].partition("-")
            start_elf_two = int(partition[0])
            end_elf_two = int(partition[2])

            # Check if one of the sections and elf is cleaning completely overlaps the other
            # Check if the starting value of one of the elf cleaning tasks lands in between the other.
            # If neither of these are met, there cannot be an overlap.
            if (start_elf_two <= start_elf_one <= end_elf_two) or (
                    start_elf_one <= start_elf_two <= end_elf_one):
                num_overlap_pairs += 1

    print(f'PART TWO: The number of overlapping pairs, completely and partially, is {num_overlap_pairs}.\n')


cleaning()

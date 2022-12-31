# This is the third day of Advent of Code 2022.

# Items are sorted in various rucksacks, which are divided evenly into two compartments.
# Some items appear in both compartments, these items have a priority which depends on its position in the alphabet.
# Part one sums up these priorities.

def rucksacks():
    part_one()
    part_two()


def part_one():
    priority_sum = 0
    priority = 0

    with open('rucksacks.txt', 'r') as f:
        true = 1
        while true:
            # Get the next line
            next_line = f.readline()
            if next_line == '': break

            # Search for matching characters in the two compartments
            i = 0;
            compartment_split = int((len(next_line) - 1) / 2)
            item_found = 0
            while i < compartment_split:
                j = compartment_split
                while j < (len(next_line) - 1):
                    if next_line[i] == next_line[j] and item_found == 0:
                        # Set the priority value properly
                        # The adjustment depends on whether the letter is capitalized or not
                        priority = ord(next_line[i])
                        if priority < 91:
                            priority -= 38
                        else:
                            priority -= 96
                        priority_sum += priority
                        item_found = 1
                    j += 1
                i += 1
    print(f'PART ONE: The priority sum for the rucksacks is {priority_sum}.\n')


# My solution of part two assumes that every group has exactly three elves.
# It also assumes that each group shares one common character.

def part_two():
    priority_sum = 0
    priority = 0

    with open('rucksacks.txt', 'r') as f:
        true = 1
        while true:
            # Get the rucksacks of the three elves.
            elfone = set(f.readline().strip())
            elftwo = set(f.readline().strip())
            elfthree = set(f.readline().strip())
            if len(elfone) == 0 or len(elftwo) == 0 or len(elfthree) == 0: break

            # Find the intersection of the three sets of characters the elves have.
            # The character that appears should be their badge.
            common_character = elfone.intersection(elfone, elftwo)
            common_character = common_character.intersection(common_character, elfthree)

            # Extract the priority of the badge
            priority = ord(common_character.pop())
            if priority < 91:
                priority -= 38
            else:
                priority -= 96
            priority_sum += priority

    print(f'PART TWO: The priority sum for the badges is {priority_sum}.\n')


rucksacks()

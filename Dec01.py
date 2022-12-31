# This is the first day of Advent of Code 2022.

# Elves are carrying a certain number of calories.
# Puzzle Input for this problem is in the file calories.txt
# Print the number of calories the elf carrying the most calories has.

def main():
    get_most_calories()


def get_most_calories():
    print(f'This is problem 1 of the December 1st Advent of Code.\n')

    # Initialize variables.
    # most_calories keeps track of the most found so far carried by an elf.
    # For part two, most_calories is now an array with three values, tracking the top three calorie counts.
    # current_calories increments whenever a number is found. If there is a space, reset to 0.

    most_calories = [0, 0, 0]
    current_calories = 0
    next_line = 'placeholder'

    # While loop: Reading lines while there are lines.
    # If a space is found, update most_calories if needed and reset current_calories.
    # Otherwise, add to current_calories.

    with open('calories.txt', 'r') as f:
        while next_line != '':
            next_line = f.readline()
            if next_line == '\n' or next_line == '':
                x = 0
                for c in most_calories:

                    if current_calories > c:
                        most_calories[x] = current_calories
                        current_calories = c
                    x = x + 1
                current_calories = 0
            else:
                current_calories += int(next_line)

    # Print out the results

    total_calories = 0
    for c in most_calories:
        total_calories += c

    print(f'PART ONE: The elf carrying the most calories has {most_calories[0]} calories')
    print(f'PART TWO: The three elves carrying the most calories have a combined total of {total_calories} calories')

main()

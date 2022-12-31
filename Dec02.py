# This is the second day of Advent of Code 2022.

# This problem is about a Rock Paper Scissors tournament.
# The file containing the encrypted key is encrypted_rps.txt
# A & X are rock, B & Y are paper, and C & Z are scissors.
# Rock is worth 1 point, Paper 2, and Scissors 3.
# A win is 6 points, a draw is 3 points, and a loss is 0 points.
# Add up the points from each round to get the total score.

def rps():
    part_one()
    part_two()


def part_one():
    next_line = 'placeholder'
    points = 0
    you = 0
    opponent = 0

    with open('encrypted_rps.txt', 'r') as f:
        true = 1
        while true:
            # Get the next line
            next_line = f.readline()
            if next_line == '': break

            # Get you and your opponent's moves
            opponent = ord(next_line[0])
            you = ord(next_line[2])

            # Calculations to determine points gained
            difference = you - opponent
            if difference == 25:
                difference -= 3
            elif difference == 21:
                difference += 3
            difference -= 22
            difference *= 3
            points += ((you - 87) + difference)

    print(
        f'PART ONE: The predicted number of points you would score if you follow the encryption is {points} points.\n')


def part_two():
    next_line = 'placeholder'
    points = 0
    round = 0
    result = 0
    opponent = 0

    with open('encrypted_rps.txt', 'r') as f:
        true = 1
        while true:
            # Get the next line
            next_line = f.readline()
            if next_line == '': break
            # print(f'The next line is {next_line}\n')

            # Get the result and your opponent's move
            opponent = ord(next_line[0])
            result = ord(next_line[2])

            # Calculation to determine points gained Calculation JUSTIFICATION -----------------------------------
            # ((result - 88) * 3): You can win, lose or draw. A loss is 0 points, a draw is 3 points, and a win is 6
            # points. Take the ASCII value of result (88, 89, 90), subtract 88 (0, 1, 2), and multiply 3 (0, 3, 6).
            # This gives points awarded by the result.
            # ((Result + Opponent - 151) % 3) + 1: The other area where you can get points is from what you choose.
            # Result + Opponent - 151 Adds Result and Opponent but with them as 1, 2, and 3 respectively.
            # Then, by modding 3 and adding 1, you obtain the points gained by your choice.
            # -------------------------------------------------------------

            round = ((result - 88) * 3) + ((result + opponent - 151) % 3) + 1
            points += round

    print(
        f'PART TWO: The predicted number of points you would score if you follow the encryption is {points} points.\n')


rps()

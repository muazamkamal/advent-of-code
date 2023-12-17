"""AoC 1, 2023."""

# Standard library imports
import pathlib
import sys
import re


def parse_data(puzzle_input):
    """Parse input."""
    return puzzle_input.split('\n')


def part1(data):
    """Solve part 1."""
    def extract_digits(row):
        found_digits = re.findall(r'\d', row)

        if len(found_digits) == 0:
            return 0

        return int(found_digits[0] + found_digits[-1])

    return sum(map(extract_digits, data))


def part2(data):
    """Solve part 2."""
    spelled_digits_dict = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
                           "eight": "8", "nine": "9", "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9"}

    def extract_spelled_digits(row):
        regex = re.compile(r'(?=(%s))' % "|".join(spelled_digits_dict.keys()))
        found_spelled_digits = re.findall(regex, row)

        if len(found_spelled_digits) == 0:
            print("missing")
            return 0

        return int(spelled_digits_dict[found_spelled_digits[0]] + spelled_digits_dict[found_spelled_digits[-1]])

    return sum(map(extract_spelled_digits, data))


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))

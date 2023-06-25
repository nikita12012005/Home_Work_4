import re


def remove_numbers_from_file(file_path):
    output_file_path = "output.txt"

    with open(file_path, "r") as input_file, open(output_file_path, "w") as output_file:
        for line in input_file:
            line_without_numbers = re.sub(r'\d+', '', line)
            output_file.write(line_without_numbers)

    print("Numbers removed and saved to '{}'".format(output_file_path))


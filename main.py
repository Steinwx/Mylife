def write_multiple_lines_to_file(file_name):
    with open(file_name, 'w') as file:
        while True:
            line = input("Enter line: ")
            file.write(line + '\n')
            more_lines = input("Are there more lines? (y/n): ")
            if more_lines.lower() != 'y':
                break

if __name__ == "__main__":
    write_multiple_lines_to_file("mylife.txt")
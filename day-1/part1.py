def read_data(file_path) -> list:
    with open(file_path, 'r') as f:
        input_data = [str(line) for line in f.readlines()]
        # Filter out the newline characters
        input_data = [line.replace('\n', '') for line in input_data]
        # Filter out the empty lines
        input_data = [line for line in input_data if line != '']
        return input_data
    
def show_data(data: list):
    for i in range(len(data)):
        print(data[i])

def parse_line(line: str, idx: int) -> int:
    first_digit, last_digit = '', ''

    # Filter out the digits
    digits = [char for char in line if char.isdigit()]
    if(len(digits) == 0):
        return 0
    
    first_digit = digits[0]
    last_digit = digits[-1]    

    if(last_digit == ''):
        last_digit = first_digit

    if(first_digit == ''):
        first_digit = last_digit

    return int(first_digit + last_digit)

if __name__ == "__main__":
    data = read_data('input.txt')
    # data = read_data('sample.txt')
    # show_data(data)

    # The newly-improved calibration document consists of lines of text; 
    # each line originally contained a specific calibration value that the Elves now need to recover. 
    # On each line, the calibration value can be found by combining the first digit and the last digit 
    # (in that order) to form a single two-digit number.

    # For example, suppose you have the following line:
    # 1abc2
    # The first digit (1) and the last digit (2) make the number 12.
    # pqr3stu8vwx
    # The first digit (3) and the last digit (8) make the number 38.

    sum = 0
    for i in range(len(data)):
        sum += parse_line(data[i], i)

    print(f"Sum: {sum}")

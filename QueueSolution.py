# failing test 3, 5, 6, 9
# did this one all on my own!
# seems different from most other people's solutions
def solution(start, length):
    matrix = generate_matrix(start, length)
    numbers = extract_numbers(matrix)
    checksum = calculate_checksum(numbers)
    return checksum

def generate_matrix(start, length):
    matrix = []
    
    for j in range(length):
        row = []
        position = length - 1 - j
        
        for i in range(length):
            row.append(start)
            start += 1
            
            if i == position:
                row.append("/")
        
        matrix.append(row)
    
    return matrix

def extract_numbers(matrix):
    numbers = []
    
    for row in matrix:
        for col in row:
            if col == "/":
                break
            numbers.append(col)
    
    return numbers

def calculate_checksum(numbers):
    result = 0
    for num in numbers:
        result ^= num
    return result

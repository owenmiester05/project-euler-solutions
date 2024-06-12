'''Find the largest palindrome made from the product of two 3-digit numbers'''
def get_largest_palindromic_number(digits: int):
    smallest_possible_number = int('1' + ('0' * (digits - 1)))
    largest_possible_number = int('9' * digits)
    largest_palindrome = 0
    for i in range(smallest_possible_number, largest_possible_number + 1):
        for j in range(i, largest_possible_number + 1):
            if i * j > largest_palindrome and str(i * j) == str(i*j)[::-1]:
                largest_palindrome = i * j
    return largest_palindrome

print(get_largest_palindromic_number(10))
            
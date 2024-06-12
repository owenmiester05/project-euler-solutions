'''By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
find the sum of the even-valued terms.'''

def get_even_numbers_in_fib_sequence(max_number):
    even_numbers = set()
    n1 = 1
    n2 = 2
    while n1 < max_number:
        temprorary_number = n1 + n2
        n1 = n2
        n2 = temprorary_number
        if n1 % 2 == 0:
            even_numbers.add(n1)
    return even_numbers

print(sum(get_even_numbers_in_fib_sequence(4000000)))

        

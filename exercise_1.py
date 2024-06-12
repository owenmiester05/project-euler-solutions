'''find the sum of all the multiples of 3 and 5 below 1000'''
def get_multiples(n):
    valid_multiples = set()
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            valid_multiples.add(i)
    return valid_multiples

print(sum(get_multiples(1000)))

        

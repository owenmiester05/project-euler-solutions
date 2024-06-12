def get_smallest_evenly_divisible_numbers(max_number: int):
    divisible_nums = []
    for i in range(1, max_number+1):
        for num in divisible_nums:
            if i % num == 0:
                divisible_nums.remove(num)
        divisible_nums.append(i)
    current = max_number
    while True:
        current += 1
        for num in divisible_nums:
            if current % num != 0:
                break
        else:
            return current
                
     
    
print(get_smallest_evenly_divisible_numbers(20))
